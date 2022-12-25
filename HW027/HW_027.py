
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
from functools import reduce

# n = int(input('Введите число элементов списка: '))
# list_1 = []

# def list(n):
#     for i in range(int(n)):
#         list_1.append(randint(1,100))
#     return list_1
# list(n)   
# print(f"Сформированный список-> {list_1}")    

# def sum (s,list_1):
#     for i in range(len(list_1)):
#         if i % 2 != 0:
#             s += list_1[i]
#     print(f"Сумма чисел на нечетных позициях равна: {s}")

# sum(0,list_1)


n = int(input("Введите число элементов списка: "))
list_1 = [randint(1, 100) for i in range(n)]

sum = reduce(lambda a, b: a+b, list_1[1::2])
print(f"Список {list_1}" + '\n' + f"Сумма элементов на нечетной позиции {sum}")
