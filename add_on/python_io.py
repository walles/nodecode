from .node_system import NodeSystem, InputSocket
from .utils import pythonify
from typing import Optional, Any


def render_value(value: Optional[Any]) -> str:
    """
    Converts a value to its Python representation.

    Args:
        value (Any): The value to convert.

    Returns:
        str: A string containing the Python representation of the value.
    """
    if value is None:
        return "None"
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, bool):
        return "True" if value else "False"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        if value == 0:
            return "0"
        return f"{value:.3f}"
    if isinstance(value, tuple):
        return f"({', '.join(map(render_value, value))})"

    raise ValueError(f"Unsupported value type: {type(value)}")


def render_input_socket(socket: InputSocket) -> str:
    if socket.source:
        incoming = socket.source
        return f"{pythonify(socket.name)}={pythonify(incoming.node.name)}.{pythonify(incoming.name)}()"

    return f"{pythonify(socket.name)}={render_value(socket.value)}"


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
        constructor = f"    {pythonify(node.name)} = {pythonify(node.type)}("

        # Add input sockets as arguments
        inputs = []
        for input_socket in node.input_sockets:
            inputs.append(render_input_socket(input_socket))
        constructor += ", ".join(inputs) + ")\n"
        python_code += constructor

    # Add the return statement for the output node
    output_node = node_system.get_output_node()
    if output_node:
        output_constructor = f"    return {pythonify(output_node.name)}("
        outputs = []
        for output_socket in output_node.output_sockets:
            outputs.append(
                f"{pythonify(output_socket.name)}={pythonify(output_socket.name)}()"
            )
        output_constructor += ", ".join(outputs) + ")\n"
        python_code += output_constructor

    return python_code
