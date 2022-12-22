

# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

from random import randint

player1 = input("Введите имя первого игрока: ")
#player2 = input("Введите имя второго игрока: ")
bot = 'BOT'
value = 80

#Выбор очередности участника
lucky = randint(0,2) 
if lucky:
    print(f"Первый ходит {player1}")
else:
    #print(f"Первый ходит {player2}")
    print(f"Первый ходит {bot}")

#Проверка корректности
def input_corr(player):
    num = int(input(f"{player}, введите количество конфет, которое возьмете от 1 до 28: "))
    while num < 1 or num > 28:
        num = int(input(f"{player}, введите корректное количество конфет: "))
    return num
    
#Игра
count1 = 0
count2 = 0
while value > 28:
    if lucky:
        k = input_corr(player1)
        count1 += k
        value -= k
        lucky = False
    else:
        #k = input_corr(player2)
        k = randint(1,28)
        print(f"BOT взял {k} конфет")
        count2 += k
        value -= k
        lucky = True
    print(f"---Осталось {value} конфет---")
        
if lucky:
    print(f"Выиграл {player1}")
else:
    #print(f"Выиграл {player2}")
    print(f"Выиграл {bot}")