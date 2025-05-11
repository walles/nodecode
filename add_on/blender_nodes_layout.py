def get_node_levels(node_system):
    levels: dict[str, int] = {}

    def visit(node, level):
        if node.name in levels:
            levels[node.name] = max(levels[node.name], level)
        else:
            levels[node.name] = level
        for out in getattr(node, "output_sockets", []):
            for target in getattr(out, "targets", []):
                visit(target.node, level + 1)

    for node in node_system.nodes:
        if all(not inp.source for inp in getattr(node, "input_sockets", [])):
            visit(node, 0)
    # Ensure all nodes are included, even if not reached in traversal (e.g., pure sink nodes)
    for node in node_system.nodes:
        if node.name not in levels:
            # Level is one higher than the max level of its input sources, or 0 if no sources
            input_levels = [
                levels.get(inp.source.node.name, 0)
                for inp in getattr(node, "input_sockets", [])
                if inp.source
            ]
            levels[node.name] = max(input_levels, default=0) + 1
    return levels


def layout_blender_nodes(node_system, blender_nodes):
    """
    Arranges Blender nodes in a left-to-right flow based on their level in the graph.
    """
    levels = get_node_levels(node_system)
    x_offset = 300

    # Group nodes by level
    level_nodes: dict[int, list[str]] = {}
    for node_name, level in levels.items():
        level_nodes.setdefault(level, []).append(node_name)
    # Assign Y positions: nodes at the same level are stacked vertically, X by level
    y_offset = 200

    def get_sort_key(node_name):
        # For each node in the system, check if this node is an input to another node at a higher level
        for node in node_system.nodes:
            for i, inp in enumerate(getattr(node, "input_sockets", [])):
                if inp.source and inp.source.node.name == node_name:
                    return i  # Sort by input socket index
        return 999  # Nodes not connected as input go last

    for level, nodes in level_nodes.items():
        # Custom sort: nodes that are inputs to downstream nodes are ordered by the socket index
        sorted_nodes = sorted(nodes, key=get_sort_key)
        for i, node_name in enumerate(sorted_nodes):
            blender_node = blender_nodes[node_name]
            blender_node.location = (
                x_offset * level,
                -y_offset * i,  # Stack nodes at the same level vertically
            )
