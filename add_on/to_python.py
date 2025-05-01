from .node_system import NodeSystem, InputSocket
from .utils import pythonify
from typing import Optional, Any


def render_float(value: float) -> str:
    if value == 0:
        return "0"

    absvalue = abs(value)
    sign = "-" if value < 0 else ""
    if absvalue < 0.000001:
        return f"{sign}{absvalue:.9f}"
    if absvalue < 0.00001:
        return f"{sign}{absvalue:.8f}"
    if absvalue < 0.0001:
        return f"{sign}{absvalue:.7f}"
    if absvalue < 0.001:
        return f"{sign}{absvalue:.6f}"
    if absvalue < 0.01:
        return f"{sign}{absvalue:.5f}"
    if absvalue < 0.1:
        return f"{sign}{absvalue:.4f}"
    if absvalue < 1:
        return f"{sign}{absvalue:.3f}"
    if absvalue < 10:
        return f"{sign}{absvalue:.3f}"
    if absvalue < 100:
        return f"{sign}{absvalue:.2f}"
    if absvalue < 1000:
        return f"{sign}{absvalue:.1f}"

    return f"{sign}{int(absvalue)}"


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
        return render_float(value)
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

    indent = "    "

    # Start with the imports
    python_code = "from nodecode.shading import *\n\n"

    # Define the main function
    python_code += "def main() -> OutputMaterial:\n"

    # Iterate over nodes in the node system in the correct order so there are no
    # forward references
    for node in node_system.get_nodes_topologically():
        # Generate the constructor for the node
        constructor = f"{indent}{pythonify(node.name)} = {pythonify(node.node_type)}(\n{indent * 2}"

        # Add input sockets as arguments
        inputs = []
        for input_socket in node.input_sockets:
            inputs.append(render_input_socket(input_socket))
        constructor += f",\n{indent * 2}".join(inputs) + ")\n\n"
        python_code += constructor

    # Add the return statement for the output node
    output_node = node_system.get_output_node()
    if not output_node:
        raise ValueError("No output node found in the node system.")

    python_code += f"{indent}return {pythonify(output_node.name)}\n"

    return python_code
