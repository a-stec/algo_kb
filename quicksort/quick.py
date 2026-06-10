# def partition(a, low, high):
#     pivot = a[high]
#     i = low - 1
    
#     for j in range(low, high):
#         if a[j] <= pivot:
#             i += 1
#             a[i], a[j] = a[j], a[i]  # Быстрый обмен значениями
            
#     a[i + 1], a[high] = a[high], a[i + 1]
#     return i + 1

# def quick_sort(a, low, high):
#     if low < high:
#         pivot_index = partition(a, low, high)
        
#         # Рекурсия
#         quick_sort(a, low, pivot_index - 1)
#         quick_sort(a, pivot_index + 1, high)

# # Пример использования:
# nums = [10, 7, 8, 7, 7, 5]
# quick_sort(nums, 0, len(nums) - 1)
# print(nums) # [1, 5, 7, 8, 9, 10]

# Не устойчивая
# Не адаптивная


def print_arr(arr, low, high):
    for i in range(low, high + 1):
        print(arr[i], end=" ")
    print()

def bite(arr, low, high):
    if low < high:
        print_arr(arr, low, high)
        bite(arr, low + 1, high - 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
bite(arr, 0, 7)
print(arr)

