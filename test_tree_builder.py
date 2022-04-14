import pytest

from tree_builder import build_tree, DataIsNotTree, TreeIsSeparated


def test_build_empty_tree():
    assert build_tree(tuple()) == {}


def test_non_tree():
    source = (
        (None, "1"),
        ("1", "2"),
        ("2", "1"),
    )

    with pytest.raises(DataIsNotTree):
        build_tree(source)


def test_separated_tree():
    source = (
        (None, "1"),
        ("2", "3"),
    )

    with pytest.raises(TreeIsSeparated):
        build_tree(source)
