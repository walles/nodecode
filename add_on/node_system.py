from typing import Any, List, Optional


class Node:
    """Represents a single node in the system."""

    def __init__(self, name: str, node_type: str) -> None:
        self.name: str = name
        self.type: str = node_type
        self.input_sockets: List[InputSocket] = []
        self.output_sockets: List[OutputSocket] = []

    def add_input_socket(self, socket: "InputSocket") -> None:
        """Adds an input socket to the node."""
        self.input_sockets.append(socket)

    def add_output_socket(self, socket: "OutputSocket") -> None:
        """Adds an output socket to the node."""
        self.output_sockets.append(socket)

    def get_output_socket(self, name: str) -> Optional["OutputSocket"]:
        """
        Finds and returns an output socket by its name.

        Args:
            name (str): The name of the output socket.

        Returns:
            Optional[OutputSocket]: The output socket if found, otherwise None.
        """
        for socket in self.output_sockets:
            if socket.name == name:
                return socket
        return None


class NodeSystem:
    """Represents a system containing multiple nodes."""

    def __init__(self) -> None:
        self.nodes: List[Node] = []

    def add_node(self, node: Node) -> None:
        """Adds a node to the system."""
        self.nodes.append(node)

    def __repr__(self) -> str:
        """Generates a human-readable description of the NodeSystem."""
        result = ["NodeSystem:"]
        for node in self.nodes:
            result.append(f"  Node: {node.name} (Type: {node.type})")
            result.append("    Input Sockets:")
            for input_socket in node.input_sockets:
                if input_socket.source:
                    source_info = f" (Source: {input_socket.source.node.name}.{input_socket.source.name})"
                else:
                    source_info = f" (Value: {input_socket.value})"
                result.append(f"      - {input_socket.name}{source_info}")
            result.append("    Output Sockets:")
            for output_socket in node.output_sockets:
                result.append(f"      - {output_socket.name}")
        return "\n".join(result)

    def get_output_node(self) -> Optional[Node]:
        """
        Finds and returns the output node in the system.

        Returns:
            Optional[Node]: The output node if found, otherwise None.
        """
        for node in self.nodes:
            if node.type == "OutputMaterial":
                return node
        return None

    def get_nodes_topologically(self) -> List[Node]:
        """
        Sorts the nodes in topological order to ensure no forward references.

        Returns:
            List[Node]: A list of nodes sorted in topological order.
        """
        sorted_nodes = []
        visited = set()

        def visit(node: Node) -> None:
            if node in visited:
                return
            visited.add(node)
            for input_socket in node.input_sockets:
                if input_socket.source:
                    visit(input_socket.source.node)
            sorted_nodes.append(node)

        for node in self.nodes:
            visit(node)

        return sorted_nodes


class Socket:
    """Base class for sockets."""

    def __init__(self, name: str, node: Node) -> None:
        self.name: str = name
        self.node: Node = node


class OutputSocket(Socket):
    """Represents an output socket."""

    def __init__(self, name: str, node: Node) -> None:
        super().__init__(name, node)


class InputSocket(Socket):
    """Represents an input socket."""

    def __init__(
        self, name: str, node: Node, value: Any, source: Optional[OutputSocket]
    ) -> None:
        super().__init__(name, node)
        self.value: Any = value
        self.source: Optional[OutputSocket] = (
            source  # Source is an OutputSocket from another node
        )
