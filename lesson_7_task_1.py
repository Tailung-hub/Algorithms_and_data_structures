# Задание №1:
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
import random


def bubble(arr):
    is_sorted = True
    for k in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        if is_sorted:
            break
        print(arr)


arr = [random.randint(-100, 99) for i in range(10)]
print(arr)
bubble(arr)
print(arr)
