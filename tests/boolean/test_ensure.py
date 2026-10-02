import pytest

from toolkit.boolean import ensure


@pytest.mark.parametrize("value", [True, 1, 0.5, "a", b"a", [0], {"a": 1}, {0}, (0,)])
def test_returns_truthy_values(value: object) -> None:
    assert ensure(value) is value


@pytest.mark.parametrize("value", [False, 0, 0.0, "", b"", None, [], {}, set(), ()])
def test_raises_with_default_message_for_falsy_values(value: object) -> None:
    with pytest.raises(ValueError, match="^Expected value to be truthy$"):
        ensure(value)


def test_raises_with_custom_message() -> None:
    with pytest.raises(ValueError, match="^User not found$"):
        ensure(None, "User not found")
