# Задача №1:
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за
# 4 квартала (т.е. 4 числа) для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import deque

numbers = int(input('Введите количество предприятий: '))
i = 0
year = deque()
companys = {}

while i != numbers:
    c_name = input(f'Введите название {i + 1} компании: ')
    for j in range(4):
        profit = int(input(f'Прибыль {j + 1} квартала: '))
        year.append(profit)
    c_sum = sum(year)
    companys[c_name] = c_sum
    i += 1

average = round((sum(companys.values()) / numbers), 2)

higher = []
lower = []
for i in companys:
    if companys.get(i) > average:
        higher.append(i)
    else:
        lower.append(i)

print(f'Компаний: {numbers}; \n'
      f'Средняя прибыль: {average}: \n'
      f'Компании с прибылью выше средней: {", ".join(higher)}; \n'
      f'Компании с прибылью ниже средней: {", ".join(lower)}. \n')
