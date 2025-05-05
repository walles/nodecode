from add_on.node_system import InputSocket, Node, NodeSystem, OutputSocket


def diffuse_material() -> NodeSystem:
    """
    Simplest possible diffuse material with two nodes, a diffuse BSDF and a
    material output.
    """
    diffuse_node = Node("Diffuse_BSDF", "BsdfDiffuse")
    diffuse_node.add_input_socket(
        InputSocket("Color", diffuse_node, (0.800, 0.800, 0.800, 1.000), None)
    )
    diffuse_node.add_input_socket(InputSocket("Roughness", diffuse_node, 0.0, None))
    diffuse_node.add_input_socket(
        InputSocket("Normal", diffuse_node, (0.0, 0.0, 0.0), None)
    )
    diffuse_node.add_input_socket(InputSocket("Weight", diffuse_node, 0.0, None))

    diffuse_bsdf_output = OutputSocket("BSDF", diffuse_node)
    diffuse_node.add_output_socket(diffuse_bsdf_output)

    output_node = Node("Material_Output", "OutputMaterial")
    output_node.add_input_socket(
        InputSocket("is_active_output", output_node, True, None)
    )
    output_node.add_input_socket(InputSocket("target", output_node, "ALL", None))
    output_node.add_input_socket(
        InputSocket("Surface", output_node, None, diffuse_bsdf_output)
    )
    output_node.add_input_socket(InputSocket("Volume", output_node, None, None))
    output_node.add_input_socket(
        InputSocket("Displacement", output_node, (0.0, 0.0, 0.0), None)
    )
    output_node.add_input_socket(InputSocket("Thickness", output_node, 0.0, None))

    node_system = NodeSystem()
    node_system.add_node(diffuse_node)
    node_system.add_node(output_node)

    return node_system
