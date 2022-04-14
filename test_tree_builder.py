import pytest

from tree_builder import build_tree, DataIsNotTree


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
