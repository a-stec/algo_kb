# Ручка TEST
def test():
    print("Test OK")

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
            bv = a[field]
            if (av < bv): # По возрастанию
                return 1 if reverse else -1
            if (av > bv): # По убыванию
                return -1 if reverse else 1
        return 0
    return compare


# Быстрая сортировка (Схема Ломуто)
def partition_lomuto(arr, low, high, compare):
    pivot = arr[high] # Опорный элемент - последний
    i = low # Указатель на место для меньшего элемента
    
    for j in range(low, high):
        if compare(arr[j], pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quicksort_lomuto(arr, low, high, compare):
    if low < high:
        pivot_index = partition_lomuto(arr, low, high, compare)
        
        quicksort_lomuto(arr, low, pivot_index - 1, compare)
        quicksort_lomuto(arr, pivot_index + 1, high, compare)

def quicksort(arr, fields="id", reverse=False):
    rules = build_rules(fields, reverse)
    compare = make_comparator(rules)

    quicksort_lomuto(arr, 0, len(arr) - 1, compare)
