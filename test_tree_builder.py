from tree_builder import build_tree


def test_build_empty_tree():
    assert build_tree(tuple()) == {}
