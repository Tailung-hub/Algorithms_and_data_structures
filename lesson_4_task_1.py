# Урок №3, задача № 5:
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение
# и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.

import random
import timeit
import cProfile


def first(size):
    arr = [random.randint(size * -10, size * 10) for _ in range(size)]
    x = min(arr)

    for i in arr:
        if x < i < 0:
            x = i
    return x, arr.index(x)


def second(size):
    arr = [random.randint(size * -10, size * 10) for _ in range(size)]

    i = 0
    index = -1
    while i < len(arr):
        if arr[i] < 0 and index == -1:
            index = i
        elif 0 > arr[i] > arr[index]:
            index = i
        i += 1
    if index != -1:
        return arr[index], index


def third(size):
    arr = [random.randint(size * -10, size * 10) for _ in range(size)]

    second_arr = []
    for i in arr:
        if i < 0:
            second_arr.append(i)
    x = int(max(second_arr))
    return x, arr.index(x)


"""
print(timeit.timeit('second(10)', number=1000, globals=globals()))     # 0.013253599999999997
print(timeit.timeit('second(100)', number=1000, globals=globals()))    # 0.1323116
print(timeit.timeit('second(1000)', number=1000, globals=globals()))   # 1.4789296
print(timeit.timeit('second(10000)', number=1000, globals=globals()))  # 14.8332454

print(timeit.timeit('first(10)', number=1000, globals=globals()))      # 0.012132499999999997
print(timeit.timeit('first(100)', number=1000, globals=globals()))     # 0.11470549999999999
print(timeit.timeit('first(1000)', number=1000, globals=globals()))    # 1.2384681
print(timeit.timeit('first(10000)', number=1000, globals=globals()))   # 12.453998499999999

print(timeit.timeit('third(10)', number=1000, globals=globals()))      # 0.011220199999999996
print(timeit.timeit('third(100)', number=1000, globals=globals()))     # 0.1143604
print(timeit.timeit('third(1000)', number=1000, globals=globals()))    # 1.2304592
print(timeit.timeit('third(10000)', number=1000, globals=globals()))   # 12.2689485
"""
# Во всех трёх случаях зависимость линейная, самый оптимальный вариант №2 и №3.

# cProfile.run('first(10)')
"""
        63 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:10(first)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:11(<listcomp>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       16    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
# cProfile.run('first(100)')
"""
         509 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:10(first)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:11(<listcomp>)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      102    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
# cProfile.run('first(1000)')
"""
         5650 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.000    0.000    0.002    0.002 lesson_3_task_5.py:10(first)
        1    0.000    0.000    0.002    0.002 lesson_3_task_5.py:11(<listcomp>)
     1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
     1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1643    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
# cProfile.run('first(10000)')
"""
 53019 function calls in 0.025 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
        1    0.000    0.000    0.025    0.025 lesson_3_task_5.py:10(first)
        1    0.004    0.004    0.024    0.024 lesson_3_task_5.py:11(<listcomp>)
    10000    0.007    0.000    0.016    0.000 random.py:200(randrange)
    10000    0.004    0.000    0.020    0.000 random.py:244(randint)
    10000    0.005    0.000    0.009    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    13012    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
# cProfile.run('second(10)')
"""
         70 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:20(second)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:21(<listcomp>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       14    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
# cProfile.run('second(100)')
"""
608 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:20(second)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:21(<listcomp>)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      102    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
# cProfile.run('second(1000)')
"""
6673 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 lesson_3_task_5.py:20(second)
        1    0.000    0.000    0.003    0.003 lesson_3_task_5.py:21(<listcomp>)
     1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
     1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1667    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
# cProfile.run('second(10000)')
"""
63083 function calls in 0.028 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.028    0.028 <string>:1(<module>)
        1    0.004    0.004    0.027    0.027 lesson_3_task_5.py:20(second)
        1    0.004    0.004    0.022    0.022 lesson_3_task_5.py:21(<listcomp>)
    10000    0.007    0.000    0.015    0.000 random.py:200(randrange)
    10000    0.004    0.000    0.018    0.000 random.py:244(randint)
    10000    0.005    0.000    0.008    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    13077    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
# cProfile.run('third(10)')
"""
60 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:35(third)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:36(<listcomp>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
# cProfile.run('third(100)')
"""
558 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:35(third)
        1    0.000    0.000    0.000    0.000 lesson_3_task_5.py:36(<listcomp>)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       49    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      102    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
# cProfile.run('third(1000)')
"""
6199 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 lesson_3_task_5.py:35(third)
        1    0.000    0.000    0.003    0.003 lesson_3_task_5.py:36(<listcomp>)
     1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
     1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
      490    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1702    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
# cProfile.run('third(10000)')
"""
58124 function calls in 0.025 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
        1    0.001    0.001    0.025    0.025 lesson_3_task_5.py:35(third)
        1    0.004    0.004    0.023    0.023 lesson_3_task_5.py:36(<listcomp>)
    10000    0.007    0.000    0.015    0.000 random.py:200(randrange)
    10000    0.004    0.000    0.019    0.000 random.py:244(randint)
    10000    0.005    0.000    0.008    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
     5044    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    13073    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
# По данным cProfile 2 и 3 варианты примерно равны и лучше, чем 1 вариант,
# так как используют меньшее количество обращений.
