# Задание №1:
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# Подсчитать, сколько было выделено памяти под переменные. Проанализировать результат и
# определить программы с наиболее эффективным использованием памяти.

import sys

# Вариант решения, в котором каждая переменная складывалась отдельно:

"""
byte_sum = 0

x = int(input('Введите трёхзначное число: '))

a = x // 100
b = x % 100 // 10
c = x % 10
sum_nums = a + b + c
multiply_nums = a * b * c
print(f'Сумма = {sum_nums}, произведение = {multiply_nums}')

byte_sum += x
byte_sum += a
byte_sum += b
byte_sum += c
byte_sum += sum_nums
byte_sum += multiply_nums
print(f'Сумма байт: {byte_sum}')
"""

# Вариант 1:
"""
x = int(input('Введите трёхзначное число: '))
a = x // 100
b = x % 100 // 10
c = x % 10

sum_nums_1 = a + b + c
multiply_nums = a * b * c
print(f'Сумма = {sum_nums_1}, произведение = {multiply_nums}')

byte_sum = sys.getsizeof(x) + sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c) + \
           sys.getsizeof(sum_nums_1) + sys.getsizeof(multiply_nums)
print(f'Сумма байт: {byte_sum}')
# Введено число: 157, сумма байт: 84
"""

# Вариант 2:
"""
byte_sum = 0
x = int(input('Число: '))
sum_nums = (x // 100) + (x % 100 // 10) + (x % 10)
multiply_nums = (x // 100) * (x % 100 // 10) * (x % 10)
print(f'Сумма = {sum_nums}, произведение = {multiply_nums}')

byte_sum = sys.getsizeof(sum_nums) + sys.getsizeof(multiply_nums)
print(f'Сумма байт: {byte_sum}')
# Введено число: 157, сумма байт: 28
"""

# Вариант 3:
"""
byte_sum = 0
x = input('Число: ')
sum_nums = 0
multiply_nums = 1
for num in x:
    sum_nums += int(num)
for num in x:
    multiply_nums *= int(num)
print(f'Сумма = {sum_nums}, произведение = {multiply_nums}')

byte_sum = sys.getsizeof(x) + sys.getsizeof(sum_nums) + sys.getsizeof(multiply_nums)
print(f'Сумма байт: {byte_sum}')
# Введено число: 157, сумма байт: 56
"""

# Лучше всего себя показал 2 вариант решения задачи, так как имеет меньше всего переменных.
# Вариант 1: 84 B, вариант 2: 28 B, вариант 3: 56 B.
# Windows 10 Pro, x64
