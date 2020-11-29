# Задание №2:
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])

    i = 0
    j = 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            arr[i + j] = left[i]
            i += 1
        else:
            arr[i + j] = right[i]
            j += 1

    while len(left) > i:
        arr[i + j] = left[i]
        i += 1
    while len(right) > j:
        arr[i + j] = right[j]
        j += 1

    return arr


arr = [random.uniform(0, 50) for i in range(10)]

print(arr)
merge_sort(arr)
print(arr)
