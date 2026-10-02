from typing import TypeVar

T = TypeVar("T")


def ensure(value: T | None, message: str = "Expected value to be truthy") -> T:
    """Return ``value`` if it is truthy, otherwise raise ``ValueError``.

    Unlike ``assert``, the check is not stripped when Python runs with ``-O``.
    The return type drops ``None``, so the result can be used without extra
    narrowing.
    """
    if not value:
        raise ValueError(message)
    return value
