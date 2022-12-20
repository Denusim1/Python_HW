# Объявите анонимную (лямбда) функцию 
# для определения вхождения в переданную ей строку фрагмента "plr". 
# То есть, функция должна возвращать True, 
# если такой фрагмент присутствует в строке и False - в противном случае.

string = input("Введите строку: ")
result = (lambda x: 'plr' in x)(string)
print(result)

# Найти НОД двух чисел.

import random 
a = random.randint(10, 1000)
b = random.randint(10, 1000)
c = [a, b]
print(c)
while max(a,b) % min(a,b) != 0:
    if a > b:
        a = a % b
    elif a < b:
        b = b % a
print(min(a,b))
