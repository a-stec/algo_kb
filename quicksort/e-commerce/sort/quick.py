import compare

# Быстрая сортировка (Схема Ломуто)
def partition_lomuto(arr, low, high, compare):
    pivot = arr[high] # Опорный элемент - последний
    i = low # Указатель на место для меньшего элемента
    
    for j in range(low, high):
        if compare(arr[j], pivot) == 1:
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
    rules = compare.build_rules(fields, reverse)
    compare = compare.make_comparator(rules)

    quicksort_lomuto(arr, 0, len(arr) - 1, compare)
