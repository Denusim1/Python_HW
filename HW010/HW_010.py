from random import randint, shuffle


n = int(input('Введите число элементов списка: '))
list_1 = []
for i in range(n):
    list_1.append(randint(-n,n+1))
print(f"Первый полученный список: {list_1}")

shuffle(list_1)
print(f"Перемешанный список: {list_1}")

#вариант2
list_2 = list_1[:]
n_length = len(list_2)
for i in range(n_length):
    index = randint(0, n_length - 1)
    temp = list_2[i]
    list_2[i] = list_2[index]
    list_2[index] = temp
print(f"Перемешанный список2: {list_2}")