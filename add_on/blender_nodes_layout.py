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
    for level, nodes in level_nodes.items():
        for i, node_name in enumerate(sorted(nodes)):
            blender_node = blender_nodes[node_name]
            blender_node.location = (
                x_offset * level,
                -y_offset * i,  # Stack nodes at the same level vertically
            )
