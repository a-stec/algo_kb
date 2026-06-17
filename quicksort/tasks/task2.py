"""
Задача 2. Группировка отрицательных и положительных чисел
Дан массив целых чисел, содержащий как отрицательные, так и положительные значения (ноль считаем положительным или нейтральным). Необходимо переставить элементы так, чтобы все отрицательные числа оказались слева, а неотрицательные — справа. Порядок внутри каждой группы не важен.

Реализуйте функцию renumsange_signs(nums), используя однопроходный алгоритм, аналогичный partition (можно взять схему Ломуто или Хоара, но без опорного элемента — просто разделить по знаку). Оцените сложность по времени и памяти.
"""

nums = []

while True:
    num = int(input('> '))
    nums.append(num)
    if num == 0:
        break

'''
Механика "Быстрой сортировки"
'''

'''
Схема Ломуто
'''
def groupLomuto(nums):
    print("BEFORE:",nums)

    N = len(nums)
    pivot = nums[N - 1]
    i = -1
    # O(N)
    for j in range(N):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            
    nums[i + 1], nums[N - 1] = nums[N - 1], nums[i + 1]

    print("AFTER:", nums)


'''
Схема Хоаре
'''
def groupHoare(nums):
    print("BEFORE:",nums)
    N = len(nums)
    pivot = nums[N - 1]
    left = -1
    right = N - 1
    # O(N)

    while True:
        left += 1
        while nums[left] < pivot:
            left += 1
        right -= 1
        while nums[right] > pivot:
            right -= 1
        
        if left >= right:
            break
        nums[left], nums[right] = nums[right], nums[left]

    nums[left], nums[N - 1] = nums[N - 1], nums[left]

    print("AFTER:", nums)

