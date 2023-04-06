from variables import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot(BOT_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open web page', web_app=WebAppInfo(url='https://agrobank.uz/uz/person')))
    await message.answer('Hello my friend', reply_markup=markup)


executor.start_polling(dp)