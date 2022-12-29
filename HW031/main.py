
from urllib import response
import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types # для указание типов

bot = telebot.TeleBot('_________________')

chat_id = '________________________'
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}


def download(url):
    resp = requests.get(url, stream=True)
    r = open("HW031/"+"1"+".jpeg", "wb")
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Показать последнбю новость на сайте securitylab.ru")

    markup.add(btn1)
    bot.send_message(message.chat.id, text= 'Бот-парсер новостей. Внизу кнопкa, нажми .',reply_markup=markup)

while True:
    url = "https://www.securitylab.ru/news/"
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    articles_cards = soup.find_all("a", class_="article-card")
    for article in articles_cards:
        article_title = article.find("h2", class_="article-card-title").text.strip()
        article_desc = article.find("p").text.strip()
        article_url = f'https://www.securitylab.ru{article.get("href")}'
        url_img = article.find('a', class_ = 'article-card inline-card')
        dow_img = 'https://www.securitylab.ru'+ article.find('img', class_='d-none').get('src')
    
        news = f"Свежая новость!\n{article_title} \n{article_desc} \nИсточник: {article_url}"
        download(dow_img)
    
    @bot.message_handler(content_types='text')
    def text(message):
        if message.text == 'Показать последнбб новость на сайте securitylab.ru':
            imadge_post= open('HW031/1.jpeg','rb')
            print(news)
            bot.send_photo(message.chat.id, imadge_post, caption = news)
       
    bot.polling()

