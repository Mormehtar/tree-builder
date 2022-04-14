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


def test_tree_is_not_separated():
    source = (
        ("1", "2"),
        (None, "1"),
    )
    expected = {"1": {"2": {}}}
    assert build_tree(source) == expected


def test_tree_big_tree():
    source = (
        ("1", "2"),
        (None, "1"),
        ("3", "4"),
        ("3", "5"),
        (None, "6"),
        ("6", "3"),
    )
    expected = {
        "1": {"2": {}},
        "6": {"3": {"4": {}, "5": {}}},
    }
    assert build_tree(source) == expected
