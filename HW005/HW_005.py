# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import os
clear = lambda: os.system('clear')
clear()
import math

ax = float(input('Введите координаты точки a по оси x: '))
ay = float(input('Введите координаты точки a по оси y: '))
bx = float(input('Введите координаты точки b по оси x: '))
by = float(input('Введите координаты точки b по оси y: '))

dist = math.sqrt((ax-bx)**2+(ay-by)**2)
print(f'Растояние между точкой A до точки B = {dist}' )