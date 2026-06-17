"""
Пакет sort.

Идея: ПОЛИТИКА (как сравнивать) и МЕХАНИЗМ (каким алгоритмом сортировать)
разделены. Политику задаёт компаратор из compare.py; механизм выбирается
параметром algo. Алгоритмы взаимозаменяемы, потому что у всех одна сигнатура
sort(arr, compare).
"""
from . import compare as _compare
from . import quick, insert

_ALGORITHMS = {
    "quick": quick.sort,    # быстрая, нестабильная
    "insert": insert.sort,  # вставками, стабильная
}


def sort(arr, by="id", reverse=False, algo="quick"):
    """Сортирует список словарей НА МЕСТЕ.

        by      — поле / список полей / список пар (поле, reverse)
        reverse — общее направление для полей, заданных строкой
        algo    — "quick" или "insert"
    """
    if algo not in _ALGORITHMS:
        raise ValueError(f"Неизвестный алгоритм: {algo!r}. Доступно: {list(_ALGORITHMS)}")

    rules = _compare.build_rules(by, reverse)
    comparator = _compare.make_comparator(rules)
    return _ALGORITHMS[algo](arr, comparator)
