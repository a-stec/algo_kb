"""
quick.py — быстрая сортировка (схема Ломуто). НЕстабильная.
Единая сигнатура: sort(arr, compare).
"""


def _partition(arr, low, high, compare):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        # Влево уходит тот, кто должен стоять раньше-или-наравне с pivot.
        if compare(arr[j], pivot) <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def _quicksort(arr, low, high, compare):
    if low < high:
        p = _partition(arr, low, high, compare)
        _quicksort(arr, low, p - 1, compare)
        _quicksort(arr, p + 1, high, compare)


def sort(arr, compare):
    _quicksort(arr, 0, len(arr) - 1, compare)
    return arr
