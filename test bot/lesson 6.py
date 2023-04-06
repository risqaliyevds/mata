import telebot
from variables import *
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot(BOT_API)
currency = CurrencyConverter()

amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi send me amount of money')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Not available value!\nTry again! Send numeric value!')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('GBP/USD', callback_data='gbp/usd')

        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Choose convert currency', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Try again! Send numeric value above 0!')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    values = call.data.upper().split('/')
    res = currency.convert(amount, values[0], values[1])
    bot.send_message(call.message.chat.id, f'Amount of converted money: {round(res, 2)}.\nYou can send amount of money to convert one more time!')
    print(currency.currencies)
    bot.register_next_step_handler(call.message, summa)

bot.polling(none_stop=True)

