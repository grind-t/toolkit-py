from collections import defaultdict
from collections.abc import Callable, Hashable, Iterable


def group_by[T, K: Hashable](
    items: Iterable[T], key: Callable[[T], K]
) -> dict[K, list[T]]:
    """Group ``items`` into lists by ``key``, keeping the order of both."""
    groups: defaultdict[K, list[T]] = defaultdict(list)
    for item in items:
        groups[key(item)].append(item)
    # a plain dict, so reading a missing key raises instead of adding a group
    return dict(groups)
