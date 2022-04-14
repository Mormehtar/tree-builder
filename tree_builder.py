from typing import Sequence, Optional, Tuple, Dict, Set


Node = Dict[str, "Node"]


class TreeBuilderException(Exception):
    ...


class DataIsNotTree(TreeBuilderException):
    ...


def build_tree(data: Sequence[Tuple[Optional[str], str]]) -> Node:
    nodes: Set[str] = set()

    for from_node, to_node in data:
        if to_node in nodes:
            raise DataIsNotTree(
                f"{to_node} is child already, data is not tree"
            )
        if from_node is not None:
            nodes.add(from_node)

    return {}
