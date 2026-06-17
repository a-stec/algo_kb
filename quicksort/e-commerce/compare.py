"""
compare.py — Политика сравнения (как решать, кто раньше).

Контракт компаратора. Функция compare(a, b) возвращает:
    < 0  -> a должен стоять РАНЬШЕ b
    = 0  -> a и b равнозначны (по всем полям из правил)
    > 0  -> a должен стоять ПОЗЖЕ b

Любой алгоритм сортировки в этом пакете умеет работать с таким компаратором.
Именно общий контракт делает алгоритмы взаимозаменяемыми.
"""


def build_rules(fields, reverse=False):
    """Приводит запись полей к списку пар (поле, reverse).

        "price"                              -> [("price", False)]
        ["status", "price"]                  -> оба поля с общим reverse
        [("status", False), ("price", True)] -> у каждого поля своё направление
    """
    if isinstance(fields, str):
        return [(fields, reverse)]

    rules = []
    for field in fields:
        if isinstance(field, tuple):
            rules.append(field)
        else:
            rules.append((field, reverse))
    return rules


def make_comparator(rules):
    """Собирает функцию сравнения по правилам"""
    def compare(a, b):
        for field, reverse in rules:
            av = a[field]
            bv = b[field]
            if av < bv:
                return 1 if reverse else -1
            if av > bv:
                return -1 if reverse else 1
        return 0
    return compare
