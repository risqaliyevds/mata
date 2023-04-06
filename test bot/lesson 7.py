from aiogram import Bot, Dispatcher, executor, types
from variables import *

#bot.polling(none_stop=True)

bot = Bot(BOT_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
#    await bot.send_message(message.chat.id, 'Hello aiogram')
    await message.answer('Hello aiogram')

@dp.message_handler(commands = ['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    site =  types.InlineKeyboardButton('site', url = 'https://agrobank.uz/uz/person')
    just_click = types.InlineKeyboardButton('nothing', callback_data='just click')
    markup.add(site, just_click)
    await message.reply('Nothing', reply_markup=markup)
@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands = ['reply'])
async def info(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('site'))
    markup.add(types.KeyboardButton('website'))
    await message.answer('hello agro world', reply_markup=markup)

executor.start_polling(dp)