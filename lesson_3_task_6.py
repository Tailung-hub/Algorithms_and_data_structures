# Задача № 6:
# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

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

sum_nums = 0
for i in array:
    if i != max_num and i != min_num:
        sum_nums += i
print(f'Сумма чисел = {sum_nums}')
