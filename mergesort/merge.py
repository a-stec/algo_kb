
# merge - Функция слияния двух подмассивов
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right): # O(N)
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# mergesort - Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

arr = [2, 3, 6, 1, 8, 4, 7, 5]
print(merge_sort(arr))
# [a] < [b]

"""
1. На слияние попадают только отсортированные списки
2. Поочередное сравнение слева направо (от наименьшего до наибольшего)
3. На слияние попадают списки равно длины (почти равно)

N * logN
"""
