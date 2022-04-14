from collections import defaultdict
from typing import Sequence, Optional, Tuple, Dict, List


Node = Dict[str, "Node"]


class TreeBuilderException(Exception):
    ...


class DataIsNotTree(TreeBuilderException):
    ...


class TreeIsSeparated(TreeBuilderException):
    ...


class EdgesContainer(object):
    __slots__ = ("children", "used")

    children: List[str]
    used: bool

    def __init__(self):
        self.children = []
        self.used = False

    def add_child(self, child_id: str):
        self.children.append(child_id)


def build_tree(data: Sequence[Tuple[Optional[str], str]]) -> Node:
    edges: Dict[str, EdgesContainer] = defaultdict(EdgesContainer)

    for from_node, to_node in data:
        edges[from_node].add_child(to_node)

    edges = dict(edges)

    result: Node = {}
    build_subtree(edges, result, None)

    for parent_id, edge_container in edges.items():
        if not edge_container.used:
            raise TreeIsSeparated(
                f"{parent_id} is not reachable from root"
            )

    return result


def build_subtree(edges: Dict[str, EdgesContainer], parent: Node, parent_id: Optional[str]):
    edge_container = edges.get(parent_id, None)
    if edge_container is None:
        return
    if edge_container.used:
        raise DataIsNotTree(f"{parent_id} is used as child by two parents")
    edge_container.used = True

    for child in edge_container.children:
        parent[child] = {}
        build_subtree(edges, parent[child], child)
