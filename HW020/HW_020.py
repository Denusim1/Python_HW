#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


with open('HW020/one.txt', 'r') as file:
   one = file.read()
   one = one[0:-4]

with open('HW020/two.txt', 'r') as file:
   two = file.read()

with open('HW020/file_end.txt', 'w', encoding='utf-8') as file:
   file.write(f'{one} + {two}')
print("Фаил сохранен, называется file_end.txt")