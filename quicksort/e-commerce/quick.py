# Ручка TEST
def test():
    print("Test OK")


def build_rules(fields, reverse):
    pass

def make_comparator(rules):
    def compare(a, b):
        for field, reverse in rules:
            av = a[field]
            bv = a[field]
            if (av < bv):
                return 1 if reverse else -1
            if (av > bv):
                return -1 if reverse else 1
        return 0
    return compare
    

# Быстрая сортировка (Схема Ломуто)
def partition_lomuto(arr, low, high, field, reverse):
    pivot = arr[high] # Опорный элемент - последний
    i = low # Указатель на место для меньшего элемента
    
    for j in range(low, high):
        if arr[j][field] > pivot[field]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quicksort_lomuto(arr, low, high, field, reverse):
    if low < high:
        pivot_index = partition_lomuto(arr, low, high, field, reverse)
        
        quicksort_lomuto(arr, low, pivot_index - 1, field, reverse)
        quicksort_lomuto(arr, pivot_index + 1, high, field, reverse)

def quicksort(arr, field="id", reverse=False):
    quicksort_lomuto(arr, 0, len(arr) - 1, field, reverse)
