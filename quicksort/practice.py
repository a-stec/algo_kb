import random

'''
Выбор pivot
'''

def get_pivot(arr, low, high, strategy="middle"):
        # 1. Выбор первого элемента
        if strategy == "first":
            return arr[low], low
        # 2. Выбор последнего элемента
        elif strategy == "last":
            return arr[high], high
        # 3. Выбор среднего элемента
        elif strategy == "middle":
            mid = (low + high) // 2
            return arr[mid], mid
        # 4. Выбор случайного элемента
        elif strategy == "random":
            idx = random.randint(low, high)
            return arr[idx], idx
        # 5. Медиана трех
        elif strategy == "median_of_three":
            mid = (low + high) // 2
            a, b, c = arr[low], arr[mid], arr[high]
            # Логика поиска медианы из трех значений
            if (a <= b <= c) or (c <= b <= a): idx = mid
            elif (b <= a <= c) or (c <= a <= b): idx = low
            else: idx = high
            return arr[idx]    

'''
Статистика
'''

comparisons = 0
swaps = 0
count = 0

def clear_stats():
    global comparisons, swaps, count
    comparisons = 0
    swaps = 0
    count = 0
    
def print_stats():
    global comparisons, swaps, count
    print(f"Сравнения: {comparisons}")
    print(f"Перемещения: {swaps}")
    print(f"Итерации: {count}")
    print()

'''
Схема Хоаре
'''

def quicksort_hoare(arr, low, high):
    if low < high:
        # Получаем индекс разделения
        pivot_index = partition_hoare(arr, low, high)
        # Рекурсивно сортируем две половины
        quicksort_hoare(arr, low, pivot_index)
        quicksort_hoare(arr, pivot_index + 1, high)
    
    return arr

def partition_hoare(arr, low, high):
    global comparisons, swaps, count
    pivot = arr[(low + high) // 2] # Выбор среднего элемента опорным
    # pivot = get_pivot(arr, low, high, "median_of_three")
    i = low - 1
    j = high + 1
    
    count += 1
    while True:
        i += 1
        comparisons += 1
        while arr[i] < pivot:
            count += 1
            i += 1
            comparisons += 1
        
        j -= 1
        comparisons += 1
        while arr[j] > pivot:
            count += 1
            j -= 1
            comparisons += 1
        
        if i >= j:
            return j
        
        swaps += 1
        # Обмен элементов
        arr[i], arr[j] = arr[j], arr[i]
    

# Пример использования:
# data = [8, 3, 1, 7, 0, 10, 2]
# data = [x for x in range(100)]
data = [x for x in range(100, 0, -1)]
print(f"Быстрая сортировка - Схема Хоаре")
print(quicksort_hoare(data, 0, len(data) - 1))
print_stats()
print()


'''
Схема Ломуто
'''

def quicksort_lomuto(arr, low, high):
    if low < high:
        # Индекс опорного элемента
        pivot_index = partition_lomuto(arr, low, high)
        
        # Рекурсивно сортируем левую и правую части
        quicksort_lomuto(arr, low, pivot_index - 1)
        quicksort_lomuto(arr, pivot_index + 1, high)
        
    return arr

def partition_lomuto(arr, low, high):
    global comparisons, swaps, count
    pivot = arr[high] # Опорный элемент - последний
    i = low # Указатель на место для меньшего элемента
    
    for j in range(low, high):
        count += 1
        comparisons += 1
        if arr[j] <= pivot:
            swaps += 1
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    swaps += 1
    # Меняем опорный элемент местами с элементом по индексу i
    arr[i], arr[high] = arr[high], arr[i]
    return i

# Пример использования:
clear_stats()
# data = [8, 3, 1, 7, 0, 10, 2]
# data = [x for x in range(100)]
data = [x for x in range(100, 0, -1)]
print(f"Быстрая сортировка - Схема Ломуто")
print(quicksort_lomuto(data, 0, len(data) - 1))
print_stats()
print()


# Best/Avg = O(N*logN)
# Worst = O(N^2)
# Пространственная сложность - O(logN)


# N*logN = 7 * 3 = 21
# 3-разбиение
