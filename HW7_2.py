'''отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке от 0 до 50'''

import random, operator
# постановка задачи

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print(f'Исходный массив:\n{array}')
# решение задачи

# разделяй

def divide(array):
    ''' суть метода сортировки слиянием сводится к разбитию массива на отдельные элементы и последующим их сравнением,
    друг с другом. Базовым случаем является массив с 1 элементов, мы рекурсивно делим  исходный массив на более мелкие массивы.
    После чего мы сравниваем с помощью функции merge_and_sort получившиеся массивы,
    результат сравнения заносится в список result'''
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = divide(array[:middle])
        right = divide(array[middle:])
    return merge_and_sort(left, right)

# и властвуй

def merge_and_sort(left, right):
    '''Сравнение производится с 0 элемента, наименьший добавляется в список result,
    наибольший сравнивается со следующим элементом, если элементов больше нет, то происходит его добавление в result'''
    result = []
    i, j = 0, 0  # индексы массивов
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    return result

print(f'Массив отсортированный методом слияния:\n{divide(array)}')