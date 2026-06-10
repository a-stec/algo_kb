def test():
    print("Test OK")

'''
Схема Ломуто
'''

def quicksort(arr, field="id", reverse=False):
    quicksort_lomuto(arr, 0, len(arr) - 1, field, reverse)

def quicksort_lomuto(arr, low, high, field, reverse):
    if low < high:
        pivot_index = partition_lomuto(arr, low, high, field, reverse)
        
        quicksort_lomuto(arr, low, pivot_index - 1, field, reverse)
        quicksort_lomuto(arr, pivot_index + 1, high, field, reverse)

def partition_lomuto(arr, low, high, field, reverse):
    pivot = arr[high] # Опорный элемент - последний
    i = low # Указатель на место для меньшего элемента
    
    if (not reverse):
        for j in range(low, high):
            if arr[j][field] <= pivot[field]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
    else:
        for j in range(low, high):
            if arr[j][field] > pivot[field]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i

# def quicksort(arr, field, reverse=False):
#     if (not reverse):
#         print("Sort ASC")
#     else:
#         print("Sort DESC")

# try:
#     quicksort([], "", False)
#     print("ok.")
# except TypeError:
#     print("error")
