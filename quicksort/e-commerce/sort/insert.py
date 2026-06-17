"""
insert.py — сортировка вставками. СТАБИЛЬНАЯ.
Та же сигнатура sort(arr, compare), поэтому взаимозаменяема с quick.sort.
"""


def sort(arr, compare):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        # Строгое '> 0' (не '>= 0') не двигает равные элементы -> сортировка стабильна.
        while j >= 0 and compare(arr[j], current) > 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr
