# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint

n = int(input('Введите число элементов списка: '))
list_1 = []
list_2 = []

def list(n):
    for i in range(int(n)):
        list_1.append(randint(1,10))
    return list_1
list(n)  
print(f"Сформированный список-> {list_1}")   

def multiplication_lst(n, lst):
    for i in range(len(lst)):
        while i < len(lst)/2 and n > len(lst)/2:
            n = n - 1
            a = lst[i] * lst[n]
            list_2.append(a)
            i += 1
multiplication_lst(n, list_1)
print(f"Результат->{list_2}")

exit()
# вариант 2
def multiplication_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    list_2 = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(f"Результат->{list_2}")
multiplication_lst( list_1)


