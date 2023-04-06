from variables import *
import telebot
import requests
import json

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! Send me your city name to get weither!')

@bot.message_handler(content_types=['text'])
def get_weither(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')

    data = json.loads(res.text)

    bot.reply_to(message, f'Current weither: {data["main"]["temp"]}')

bot.polling(none_stop=True)