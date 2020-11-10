# Задача №3:
# В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_num = MAX_ITEM
max_num = MIN_ITEM

for i in array:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i

print(f'Мин. число: {min_num}, макс. число: {max_num}')

index_min_num = array.index(min_num)
index_max_num = array.index(max_num)

array.insert(index_min_num, array.pop(array.index(max_num)))
array.insert(index_max_num, array.pop(array.index(min_num)))
print(array)
