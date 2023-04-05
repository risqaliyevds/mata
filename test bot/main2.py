import telebot
import sqlite3
from variables import *

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands = ['start'])
def start_message(message):
    conn = sqlite3.connect('agro.sql')
    cur = conn.cursor()

    cur.execute('create table if not exists users (id int auto_increment primary key,name varchar(50),pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id,
                     'Hello send me your name:')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    pass

bot.polling(none_stop=True)
