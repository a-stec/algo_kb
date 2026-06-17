def quicksort_lomuto(arr, low, high, k):
    if low < high:
        pivot_index = partition_lomuto(arr, low, high)
        
        if (k == pivot_index + 1):
            return arr[pivot_index]
        elif (k < pivot_index + 1):
            return quicksort_lomuto(arr, low, pivot_index - 1, k)
        else:
            return quicksort_lomuto(arr, pivot_index + 1, high, k)
    elif low == high:
        return arr[low]


def partition_lomuto(arr, low, high):
    pivot = arr[high] # Опорный элемент - последний
    i = low # Указатель на место для меньшего элемента
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # Меняем опорный элемент местами с элементом по индексу i
    arr[i], arr[high] = arr[high], arr[i]
    return i

k = 4
arr = [-7, -4, 5, 2, 1, -3, 6, 0]
print(quicksort_lomuto(arr, 0, len(arr) - 1, k))
