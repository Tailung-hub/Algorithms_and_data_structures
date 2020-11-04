# https://drive.google.com/file/d/1CTmROh62XtsTFIxQa7We6QliuWmpFcbI/view?usp=sharing

# Задание №1:
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input('Введите трёхзначное число: '))

a = x // 100
b = x % 100 // 10
c = x % 10

sum = a + b + c
multiply = a * b * c

print(f'Сумма = {sum}, произведение = {multiply}')
