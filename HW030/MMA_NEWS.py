from email import message
from urllib import response
import requests
from bs4 import BeautifulSoup
import telebot
from time import sleep
from telebot import types # для указание типов

bot = telebot.TeleBot('___________________')

chat_id = '____________'
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/1")
    btn2 = types.KeyboardButton("/2")
    btn3 = types.KeyboardButton("/3")
    btn4 = types.KeyboardButton("/4")
    btn5 = types.KeyboardButton("/5")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text= 'выбери новость',reply_markup=markup)


while True:
    list_card_url = []
    list_card_url_2 = []
    list_card_url_3 = []
    list_card_url_4 = []

    
    hashtegs = '#Заявка_на_участие'+'\n'+'@vershinapromotion'
    

    # Загрузчики
    def download(url):
        resp = requests.get(url, stream=True)
        r = open("/home/kali/Рабочий стол/bot_mma/images/"+"1"+".jpeg", "wb")
        for value in resp.iter_content(1024*1024):
            r.write(value)
        r.close()

    def download_2(url_2):
        resp = requests.get(url_2, stream=True)
        r = open("/home/kali/Рабочий стол/bot_mma/images/"+"2"+".jpeg", "wb")
        for value in resp.iter_content(1024*1024):
            r.write(value)
        r.close()

    def download_3(url_3):
        resp = requests.get(url_3, stream=True)
        r = open("/home/kali/Рабочий стол/bot_mma/images/"+"3"+".jpeg", "wb")
        for value in resp.iter_content(1024*1024):
            r.write(value)
        r.close()
    
    def download_4(url_4):
        resp = requests.get(url_4, stream=True)
        r = open("/home/kali/Рабочий стол/bot_mma/images/"+"4"+".jpg", "wb")
        for value in resp.iter_content(1024*1024):
            r.write(value)
        r.close()





    url = 'https://fightnews.info/mma'
    url_2 = 'https://www.championat.com/boxing/_mma.html'
    url_3 = 'https://www.bloodandsweat.ru/category/news/'
    url_4 = 'https://fighttime.ru/'


    links = '______________________________'+'\n' + 'Источник:'+ " " + 'fightnews.info'
    links_2 = '______________________________'+'\n' + 'Источник:'+ " " + 'championat.com'
    links_3 = '______________________________'+'\n' + 'Источник:'+ " " +  'bloodandsweat.ru'
    links_4 = '______________________________'+'\n' + 'Источник:'+ " " + 'fighttime.ru'
   

    # Первая новость

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_ = 'row post-list mb-3')
    news = data.find('a', class_= 'page-title').get('href')
    list_card_url.append(news)


    for news in list_card_url:
        response = requests.get(news, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_ = 'row mb-4')
        text_blok = data.find('div', class_ = "content").text
                

        url_img = data.find('img', class_ = 'thumbnail').get('src') 
        print(url_img + "\n\n" +text_blok)
        download(url_img)
        


        

        # Вторая новость

    response = requests.get(url_2, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data_2 = soup.find('div', class_ = 'article-preview')
    news_2_url = data_2.find('a', class_='article-preview__title').get('href')
    list_card_url_2.append(news_2_url)

    for news in list_card_url_2:
        response = requests.get(news_2_url, headers=headers)
        soup_2 = BeautifulSoup(response.text, 'lxml')
        data_2 = soup_2.find('article', class_ = 'article lp_article_content')
        content_2 = data_2.find('div', class_= 'article-content js-content-banners-wrapper js-copyright-content js-loyalty-article-content')
        content_3 = content_2.find('p').text
            

            
        conteiner = data_2.find('div', class_='article-head__photo')
        url_img_2 = conteiner.find('img').get('src') 
        print(url_img_2 + "\n\n" + content_3)
        download_2(url_img_2)



        # Третья новость

    response = requests.get(url_3, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data3 = soup.find('div', class_ = 'news-block-item clearfix')
    news3 = data3.find('span', class_= 'content-text-more')
    blok3 = news3.find('a').get('href')
    list_card_url_3.append(blok3)


    for news3 in list_card_url_3:
        response = requests.get(blok3, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data3 = soup.find('span', class_ = 'content_wrap').text
        blok_img = soup.find('span', class_ = 'content_wrap')
            

        url_img_3 = blok_img.find('a').get('href')  
        print(url_img_3 + "\n\n" +data3)
        download_3(url_img_3)
    
    
        # четвертая новость

    response = requests.get(url_4, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data4 = soup.find('li', class_ = 'item_even')
    news4 = data4.find('div', class_= 'widget-full-list-text left relative')
    blok4 = 'https://fighttime.ru' + news4.find('a').get('href')
    list_card_url_4.append(blok4)


    for news4 in list_card_url_4:
        response = requests.get(blok4, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data4 = soup.find('div', class_ = 'itemFullText').text
        blok_img = soup.find('div', {"id": "feat-img-reg"}, class_ = 'relative')
            

        url_img_4 = 'https://fighttime.ru' + blok_img.find('img').get('src')  
        print(url_img_4 + "\n\n" +data4)
        download_4(url_img_4)
    sleep(30)
    

    data5 = ' 🤜 ЗАЯВКА НА УЧАСТИЕ 🤛\n\n🥊ВЕРШИНА - новый современный промоушн!\nНаша лига для сильных и смелых бойцов! Мы молодая профессиональная организация по ММА - открываем набор проыессиональных и начинающих бойцов в нашу топовую команду!!!\n\n⏱Совсем скоро состоится кастинг. Если ты хочешь стать популярным, улучшить свое финансовое положение, вырасти как профессиональный спортсмен и стать чемпионом.\nТебе к нам!!!💪\n\n👇Заполняй анкету, сними видеоролик о себе и отправляй скорее! Спеши количество участников ограничено.\nПокори ВЕРШИНУ!!! '
    
    @bot.message_handler(commands=['1'])
    def text(message):
        imadge_post= open('/home/kali/Рабочий стол/bot_mma/images/1.jpeg','rb')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Отправить новость', callback_data=1))


        bot.send_photo(message.chat.id, imadge_post,caption='🤜🤛'+ text_blok +"💪"+"\n"+ links +"\n"+ hashtegs,reply_markup=markup)
            
    @bot.message_handler(commands=['2'])
    def text(message):
        imadge_post_2= open('/home/kali/Рабочий стол/bot_mma/images/2.jpeg','rb')
        markup_2 = telebot.types.InlineKeyboardMarkup()
        markup_2.add(telebot.types.InlineKeyboardButton(text='Отправить новость', callback_data=2))

        bot.send_photo(message.chat.id, imadge_post_2,caption='🤜🤛'+ content_3 +"🥊"+"\n"+ links_2 +"\n"+ hashtegs,reply_markup=markup_2)


    @bot.message_handler(commands=['3'])
    def text(message):
        imadge_post3= open('/home/kali/Рабочий стол/bot_mma/images/3.jpeg','rb')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Отправить новость', callback_data=3))                               

        bot.send_photo(message.chat.id, imadge_post3,caption='👆'+ data3+"👊"+"\n"+ links_3 +"\n"+ hashtegs,reply_markup=markup)

    @bot.message_handler(commands=['4'])
    def text(message):
        imadge_post4= open('/home/kali/Рабочий стол/bot_mma/images/4.jpg','rb')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Отправить новость', callback_data=4))                               

        bot.send_photo(message.chat.id, imadge_post4,caption='👆'+ data4+"👊"+"\n"+ links_4 +"\n"+ hashtegs, reply_markup=markup)

    @bot.message_handler(commands=['5'])
    def text(message):
        imadge_post5= open('/home/kali/Рабочий стол/bot_mma/images/6.jpg','rb')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Подать заявку',url= "https://fightersprofile.ru/", callback_data=5)) 
        markup.add(telebot.types.InlineKeyboardButton(text='Отправить новость', callback_data=5))   


        bot.send_photo(message.chat.id, imadge_post5,caption= data5+"👊", reply_markup=markup)
    


    
        # Переаылка в канал

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call): 
        if call.data == '1':
            bot.send_photo( chat_id ='-____', photo= open('/home/kali/Рабочий стол/bot_mma/images/1.jpeg','rb'), caption='🤜🤛'+ text_blok +"💪"+"\n"+ links +"\n"+ hashtegs)
        elif call.data == '2':
            bot.send_photo( chat_id ='-_______', photo= open('/home/kali/Рабочий стол/bot_mma/images/2.jpeg','rb'), caption='🤜🤛'+ content_3+"🥊"+"\n"+ links_2 +"\n"+ hashtegs)
        elif call.data == '3':
            bot.send_photo( chat_id ='-_______', photo= open('/home/kali/Рабочий стол/bot_mma/images/3.jpeg','rb'), caption='👆'+ data3+"👊"+"\n"+ links_3 +"\n"+ hashtegs)
        elif call.data == '4':
            bot.send_photo( chat_id ='-_____', photo= open('/home/kali/Рабочий стол/bot_mma/images/4.jpg','rb'), caption='💪'+ data4+"🤜🤛"+"\n"+ links_4 +"\n"+ hashtegs)
        elif call.data =='5':
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='Подать заявку',url= "https://fightersprofile.ru/", callback_data=5)) 
            
            bot.send_photo(chat_id ='-_______', photo= open('/home/kali/Рабочий стол/bot_mma/images/6.jpg','rb'), caption= data5+"🤜🤛"+"\n"+ hashtegs, reply_markup=markup)

        




    bot.polling()
        