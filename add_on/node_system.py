from typing import Any, List, Optional

class Node:
    """Represents a single node in the system."""
    def __init__(self, name: str, node_type: str) -> None:
        self.name: str = name
        self.type: str = node_type
        self.input_sockets: List[InputSocket] = []
        self.output_sockets: List[OutputSocket] = []

    def add_input_socket(self, socket: 'InputSocket') -> None:
        """Adds an input socket to the node."""
        self.input_sockets.append(socket)

    def add_output_socket(self, socket: 'OutputSocket') -> None:
        """Adds an output socket to the node."""
        self.output_sockets.append(socket)

class NodeSystem:
    """Represents a system containing multiple nodes."""
    def __init__(self) -> None:
        self.nodes: List[Node] = []

    def add_node(self, node: Node) -> None:
        """Adds a node to the system."""
        self.nodes.append(node)

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
    def __init__(self, name: str, node: Node, value: Any, source: Optional[OutputSocket] = None) -> None:
        super().__init__(name, node)
        self.value: Any = value
        self.source: Optional[OutputSocket] = source  # Source is an OutputSocket from another node
