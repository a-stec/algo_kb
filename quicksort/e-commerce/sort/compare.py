# Построение правил для сортировки массива по полям
def build_rules(fields, reverse):
    if isinstance(fields, str):
        return [(fields, reverse)]
    
    rules = []
    for field in fields:
        rules.append((field, reverse))
    return rules

# Строение функции для сравнения значений в Алгоритме Быстрой сортировки
def make_comparator(rules):
    def compare(a, b):
        for field, reverse in rules:
            av = a[field]
            bv = b[field]
            if (av < bv): # По возрастанию
                return 1 if reverse else -1
            if (av > bv): # По убыванию
                return -1 if reverse else 1
        return 0
    return compare
