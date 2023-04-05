import asyncio
import webbrowser
import telebot
from telebot import types
from variables import *
import sys

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands=['start'])

def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    r = ['Jismoniy shaxslar',
         'Korporativ mijozlar']
    markup.row(types.KeyboardButton(r[0]), types.KeyboardButton(r[1]))
    bot.send_message(message.chat.id,
                     f'Hello! <b>{message.from_user.first_name}</b>',
                     parse_mode='html',
                     reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Jismoniy shaxslar':
        bot.send_message(message.chat.id, f'Jismoniy shaxslar --- working')
    elif message.text == 'Korporativ mijozlar':
        bot.send_message(message.chat.id, f'Korporativ mijozlar --- working')

@bot.message_handler(content_types=['photo'])
def reply_to_photo(message):
    markup = types.InlineKeyboardMarkup()
    r = [types.InlineKeyboardButton('Web site', url='https://agrobank.uz/uz/person'),
         types.InlineKeyboardButton('Delate photo', callback_data='delate'),
         types.InlineKeyboardButton('Edit text', callback_data='edit')]

    markup.row(r[0])
    markup.row(r[1], r[2])
    bot.reply_to(message, 'Agrobank website', reply_markup = markup)


@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'delate':
        bot.delete_message(callback.message.chat.id,
                           callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text',
                              callback.message.chat.id,
                              callback.message.message_id)


bot.polling(none_stop=True)