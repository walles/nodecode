from .node_system import NodeSystem


def convert_to_python(node_system: NodeSystem) -> str:
    """
    Converts a NodeSystem into a Python script representation.

    Args:
        node_tree (NodeSystem): The node system to convert.

    Returns:
        str: A string containing the Python script representation of the node system.
    """
    # Start with the imports
    python_code = "from nodecode.shading import *\n\n"

    # Define the main function
    python_code += "def main():\n"

    # Iterate over nodes in the node system
    for node in node_system.nodes:
        # Generate the constructor for the node
        constructor = f"    {node.name} = {node.type}("

        # Add input sockets as arguments
        inputs = []
        for input_socket in node.input_sockets:
            if input_socket.source:
                linked_output = input_socket.source
                inputs.append(
                    f"{input_socket.name}={linked_output.node.name}.{linked_output.name}()"
                )
            else:
                inputs.append(f"{input_socket.name}={input_socket.value}")

        constructor += ", ".join(inputs) + ")\n"
        python_code += constructor

    # Add the return statement for the output node
    output_node = node_system.get_output_node()
    if output_node:
        output_constructor = f"    return {output_node.name}("
        outputs = []
        for output_socket in output_node.output_sockets:
            outputs.append(f"{output_socket.name}={output_socket.name}()")
        output_constructor += ", ".join(outputs) + ")\n"
        python_code += output_constructor

    return python_code
