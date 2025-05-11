import ast
from .node_system import NodeSystem, Node, InputSocket, OutputSocket
from typing import Optional, Dict, Any


def convert_from_python(nodecode_py: str) -> NodeSystem:
    # FIXME: Check for multiple main() functions
    # FIXME: Check for not having an output node

    tree = ast.parse(nodecode_py)

    return_me = NodeSystem()

    # Find the main() function
    main_function: Optional[ast.FunctionDef] = None
    for ast_node in tree.body:
        if isinstance(ast_node, ast.FunctionDef) and ast_node.name == "main":
            main_function = ast_node
    if main_function is None:
        raise ValueError("No main() function found in the provided code.")

    names_to_nodes: Dict[str, Node] = {}
    for ast_node in main_function.body:
        if isinstance(ast_node, ast.Return):
            break

        if not isinstance(ast_node, ast.Assign):
            raise ValueError("Only assignment statements are supported in main()")

        if len(ast_node.targets) != 1 or not isinstance(ast_node.targets[0], ast.Name):
            raise ValueError("Only simple variable assignments are supported")
        variable_name = ast_node.targets[0].id

        if not isinstance(ast_node.value, ast.Call):
            raise ValueError("Only function calls are supported as assignment values")
        function_call: ast.Call = ast_node.value
        assert isinstance(function_call.func, ast.Name)
        function_name = function_call.func.id

        node = Node(variable_name, function_name)
        names_to_nodes[variable_name] = node
        return_me.add_node(node)

        if len(function_call.args) != 0:
            raise ValueError("Only keyword arguments are supported in function calls")

        for keyword in function_call.keywords:
            arg_name = keyword.arg
            assert arg_name is not None, "Keyword arguments expected to have names"

            if isinstance(keyword.value, ast.Call):
                node.add_input_socket(
                    InputSocket(
                        arg_name,
                        node,
                        None,
                        parse_input_source(names_to_nodes, keyword.value),
                    )
                )
                continue

            node.add_input_socket(
                InputSocket(arg_name, node, parse_input_value(keyword.value), None)
            )

    return return_me


def parse_input_source(
    names_to_nodes: Dict[str, Node], value: ast.Call
) -> OutputSocket:
    assert isinstance(value.func, ast.Attribute)
    assert isinstance(value.func.value, ast.Name)
    source_node_name = value.func.value.id
    source_node = names_to_nodes[source_node_name]
    source_socket_name = value.func.attr
    source_socket = source_node.get_output_socket(source_socket_name)
    if not source_socket:
        source_socket = OutputSocket(source_socket_name, source_node)
        source_node.add_output_socket(source_socket)
    return source_socket


def parse_input_value(value: ast.AST) -> Optional[Any]:
    if isinstance(value, ast.Tuple):
        return tuple(parse_input_value(elt) for elt in value.elts)
    if isinstance(value, ast.Constant):
        return value.value

    raise ValueError(f"Unsupported value type: {type(value)}")
