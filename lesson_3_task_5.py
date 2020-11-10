# Задача №5:
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение
# и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.
import random

SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

x = MIN_ITEM
for i in array:
    if x < i < 0:
        x = i
print(f'Число: {x}, индекс: {array.index(x)}')
