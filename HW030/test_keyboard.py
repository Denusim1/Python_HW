from http import server
from unicodedata import name
from urllib import request
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, EMPTY_KEYBOARD, PhotoMessageUploader
from random import randint
from time import sleep
from loguru import logger



import requests
logger.disable("vkbottle")


bot = Bot(token="_______________________________")



keyboard = Keyboard(one_time=False, inline=True)
keyboard.add(Text("Пластиковые окна", {"cmd": "eat"}), color=KeyboardButtonColor.NEGATIVE).row()
keyboard.add(Text("Остекление балкона/лоджии", {"cmd": "eat"}), color=KeyboardButtonColor.NEGATIVE).row()
keyboard.add(Text("Натяжной потолок", {"cmd": "eat"}), color=KeyboardButtonColor.NEGATIVE).row()
keyboard.add(Text("Входная/межкомнатные двери", {"cmd": "eat"}), color=KeyboardButtonColor.NEGATIVE)


new_keyboard = Keyboard(one_time=False, inline=True)
new_keyboard.add(Text("Квартира", {"cmd": "next"}), color=KeyboardButtonColor.NEGATIVE).row()
new_keyboard.add(Text("Дом", {"cmd": "next"}), color=KeyboardButtonColor.NEGATIVE).row()
new_keyboard.add(Text("Другое", {"cmd": "next"}), color=KeyboardButtonColor.NEGATIVE)




@bot.on.message(text="Да")
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Добрый день, {}!<br>Cейчас Вам прийдет купон на скидку 60% и бесплатную доставку!💥<br><br>Мы зададим Вам всего два вопроса и сразу подарим купон🙃<br><br>Первый вопрос: подскажите,пожалуйста, что Вас интересует?😊<br><br>Выберите вариант, нажав кнопку ниже👇".format(users_info[0].first_name),keyboard=keyboard)

@bot.on.message(payload={"cmd": "eat"})
async def next_handler(message: Message):
    await message.answer(f"Отлично!😊Подскажите, пожалуйста, где необходим монтаж?<br><br>Выберите вариант, нажав на кнопку👇", keyboard=new_keyboard)
	

@bot.on.message(payload={"cmd": "next"})
async def eat_handler(message: Message):
    namber_kupon = randint(246,918)
    await message.answer(f"Отлично!👏Вот Ваш купон №"+ str(namber_kupon) +" на скидку 60% и бесплатную доставку!😉")
    photo_upd = PhotoMessageUploader(bot.api)
    photo = await photo_upd.upload("HW030/kupon.jpg")
    
    await message.answer( attachment=photo)
    sleep(0.5)
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("{}, оставьте, пожалуйста, свой номер телефона, чтобы мы закрепили за ним номер купона🦋<br>👇".format(users_info[0].first_name))

@bot.on.message()
async def fin_handler(message: Message):

    phone = message.text
    if phone.isdigit():
        if len(phone) == 11: 
            users_info = await bot.api.users.get(message.from_id)
            
            await message.answer("Ваш купон закреплен! <br>{}, в ближайшее время с Вами свяжется наш специалист! <br>Хорошего Вам дня😉".format(users_info[0].first_name))
            
            #Отправка в телеграмм
            token = '_____'
            chat_id = '-____________'
            text = phone
            users_info = await bot.api.users.get(message.from_id)
            
            url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" "Имя получившего купон: {}".format(users_info[0].first_name)+"\n"+"\n" + "Телефон: "+text
            results = requests.get(url_req)
            print(results.json())
               
        else:
            users_info = await bot.api.users.get(message.from_id)
            await message.answer("{}, Кажется тут ошибка! Начните с цифры 8 и не используйте пробелы, дефисы и скобки)".format(users_info[0].first_name))
    else:
        users_info = await bot.api.users.get(message.from_id)
        await message.answer("{}, Кажется Вы используете буквы вместо цифр😉!<br>Попробуйте снова!".format(users_info[0].first_name))

bot.run_forever()




