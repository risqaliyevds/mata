import telebot
import sqlite3
from variables import *

bot = telebot.TeleBot(BOT_API)
name = None

@bot.message_handler(commands = ['start'])
def start_message(message):
    conn = sqlite3.connect('agro.sql')
    cur = conn.cursor()

    cur.execute('create table if not exists users (id int auto_increment primary key,user_name varchar(50),user_password varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id,
                     'Hello send me your name:')
#    bot.send_message(message.chat.id,
#                     message)
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Send password:')
    bot.register_next_step_handler(message, user_password)

def user_password(message):
    password = message.text.strip()

    conn = sqlite3.connect('agro.sql')
    cur = conn.cursor()

    cur.execute("insert into users (user_name, user_password) values ('%s', '%s')" % (message.from_user.first_name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('List of users', callback_data='users'))
    bot.send_message(message.chat.id,
                     f'Hello, {message.from_user.first_name.split(" ")[0]} ({name}).'
                     f'\nYou registrated succesfuly', reply_markup=markup)


@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    conn = sqlite3.connect('agro.sql')
    cur = conn.cursor()

    cur.execute('select * from users')
    users = cur.fetchall()

    info = ""
    for i in users:
        info += f'user_id: {i[0]}, user_name: {i[1]}, user_password: {i[2]}\n'

    bot.send_message(call.message.chat.id, info)

    cur.close()
    conn.close()


bot.polling(none_stop=True)
