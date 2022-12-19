#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень многочлена: '))


def func(k):
    with open('HW019/file.txt', 'w') as data:
        for i in range(k, -1, -1):
            koef = randint(0, 101)
            #print(koef)
            if i > 0:
                if koef > 0:
                    data.write(f'{str(koef)}x^{str(i)} + ')
            else:
                if koef > 0:
                    data.write(f'{str(koef)} = 0')
                else:
                    data.write(' = 0')
func(k)