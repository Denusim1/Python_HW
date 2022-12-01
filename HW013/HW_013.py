# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import uniform

n = int(input('Введите число элементов списка: '))
list_1 = []
list_2 = []

def list(n):
    for i in range(int(n)):
        f = uniform(0, 9)
        list_1.append(round(f, 1))
    return list_1
list(n)  
print(f"Сформированный список-> {list_1}")  

def fract_part(lst):
    for i in lst:
        list_2.append(round(i%1,2))        
    return list_2
fract_part(list_1)

print(f"Дробные части-> {list_2}")
print(f"Результат -> {max(list_2) - min(list_2)}")


exit()
#вариант2
def fract_part(lst):
    list_2 = [round(i%1,2) for i in lst if i%1 != 0]
    print(f"Дробные части-> {list_2}")  

fract_part(list_1)
print(f"Результат -> {max(list_2) - min(list_2)}")

