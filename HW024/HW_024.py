#1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
#пример - 8 11 0 -23 140 1 => 11 -23

print(*filter(lambda x: len(str(abs(int(x)))) == 2, input("Введите числа: ").split()))

#Дан список, вывести отдельно буквы и цифры.
a = ( "a", 'b', '2', '3' ,'c')
b = ( 'a' , 'b' , 'c')
c = ( '2', '3')

print(*filter(str.isalpha, a))
print(*filter(str.isdigit, a))

#Преобразовать набора списков 
users = ['user1','user2','user3','user4','user5'] 
ids = [4, 5, 9, 14, 7] 
salary = [111,222,333] 

a,b,c = map(list,zip(users,ids,salary))
print(a,b,c, sep = "\n")
a,b,c = map(list,zip(a,b,c))
print(a,b,c, sep = "\n")