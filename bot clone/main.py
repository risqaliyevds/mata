import sqlite3
from variables import *
from markups import *

BOT_LANG = None

# Connect to the SQLite database
conn = sqlite3.connect('users.db')
# Create the users table
with conn:
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            user_name VARCHAR(50),
            phone_number VARCHAR(15),
            username VARCHAR(25)
        )
    """)

bot = telebot.TeleBot(BOT_API)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'🇺🇿 Assalomu alekum qulay tilni tanlang!\n🇷🇺 Привет, выбери подходящий язык!',
                     reply_markup=choose_lang())


@bot.message_handler(content_types=['text'])
def user_checker(message):
    chat_id = message.chat.id
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_id=?", (chat_id,))
    user = cur.fetchone()

    global BOT_LANG
    if message.text == '🇺🇿 O\'zbek':
        BOT_LANG = 'uz'
    elif message.text == '🇷🇺 Русский':
        BOT_LANG = 'ru'

    if user:
        text = {'uz' : 'Sizni qayta kurganimdan xursandmiz!',
                'ru' : 'Рад, что ты вернулся!'}
        msg = bot.send_message(chat_id, f"{text[BOT_LANG]}",
                               reply_markup=main_page_markup(BOT_LANG))

        bot.register_next_step_handler(msg, first_panel)

    else:
        text = {'uz' : 'Telefon raqamingizni yuboring:',
                'ru' : "Отправьте свой номер телефона:"}
        bot.send_message(chat_id, f'{text[BOT_LANG]}',
                         reply_markup=get_phone_number(BOT_LANG))

@bot.message_handler(content_types=['contact'])
def contact(message):
    chat_id = message.chat.id
    phone_number = message.contact.phone_number
    first_name = message.from_user.first_name
    username = message.from_user.username
    conn = sqlite3.connect('users.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (chat_id, first_name, phone_number, username))

    text = {'uz' : 'Botimizga xush kelibsiz!\n',
            'ru' : "Отправьте свой номер телефона:\n"}

    msg = bot.send_message(chat_id, f"{text[BOT_LANG]}",
                           reply_markup=main_page_markup(BOT_LANG))

    bot.register_next_step_handler(msg, first_panel)

def first_panel(message):
    chat_id = message.chat.id
    text = {'uz': 'Kerakli bo\'limni tanlang',
            'ru': "-- Kerakli bo\'limni tanlang --"}
    if message.text in ('👪Jismoniy shaxslar', '👪Частным клиентам'):
        msg_individuals = bot.send_message(chat_id, f'{text[BOT_LANG]}',
                                           reply_markup=individuals(BOT_LANG))
        bot.register_next_step_handler(msg_individuals, individuals_panel)

    elif message.text in ('🏭Korporativ mijozlarga', '🏭Корпоративным клиентам'):
        bot.send_message(chat_id, f'{text[BOT_LANG]}',
                         reply_markup=corporate_clients(BOT_LANG))
    elif message.text in ('📍 Manzillar', '📍 Адреса'):
        bot.send_message(chat_id, f'{text[BOT_LANG]}',
                         reply_markup=map(BOT_LANG))
    elif message.text in ('💵Valyuta kurslari', '💵Курсы валют'):
        if BOT_LANG == 'uz':
            file = open('Image/kurs_uz.jpg', 'rb')
            bot.send_photo(chat_id, file,
                           reply_markup=currancy(BOT_LANG))
        else:
            file = open('Image/kurs_ru.jpg', 'rb')
            bot.send_photo(chat_id, f'Image/kurs_ru.jpg',
                           reply_markup=currancy(BOT_LANG))
    elif message.text in ('🌍 Yangiliklar', '🌍 Новости'):
        bot.send_message(chat_id, 'Xozircha ushbu bulim faol emas (status: 200)')

    elif message.text in ('🏦 Bog\'lanish', '🏦 Связаться'):
        bot.send_message(chat_id, 'Xozircha ushbu bulim faol emas (status: 200)')

    elif message.text in ('⚙️ Sozlamalar', '⚙️ Настройки'):
        bot.send_message(chat_id, f'{text[BOT_LANG]}',
                         reply_markup=language(BOT_LANG))

def individuals_panel():













bot.polling(non_stop = True)

