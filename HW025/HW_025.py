
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

n = float(input('Введите число: '))                                                  
s = 0
for i in str(n):
    if i != '.':
        s+= int(i)
print(s)
  


print(sum(map(int, input('Введите число: ').replace('.', ''))))