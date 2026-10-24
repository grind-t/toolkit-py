from toolkit.array import group_by


def test_groups_items_by_key_in_order() -> None:
    words = ["apple", "bob", "avocado", "cat", "banana"]
    assert group_by(words, lambda word: word[0]) == {
        "a": ["apple", "avocado"],
        "b": ["bob", "banana"],
        "c": ["cat"],
    }


def test_returns_empty_dict_for_no_items() -> None:
    assert group_by([], len) == {}


def test_result_is_a_plain_dict() -> None:
    assert type(group_by([1], str)) is dict
