import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

def choose_lang():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    item1 = KeyboardButton("🇺🇿 O'zbek")
    item2 = KeyboardButton("🇷🇺 Русский")
    markup.add(item1, item2)
    return markup


def main_page_markup(lang):

    bottons = {'uz' : ['👪Jismoniy shaxslar', '🏭Korporativ mijozlarga', '📍 Manzillar',
                       '💵Valyuta kurslari', '🌍 Yangiliklar', '🏦 Bog\'lanish', '⚙️ Sozlamalar'],
               'ru' : ['👪Частным клиентам', '🏭Корпоративным клиентам', '📍 Адреса', '💵Курсы валют',
                       '🌍 Новости', '🏦 Связаться', '⚙️ Настройки']}

    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    item1 = KeyboardButton(bottons[lang][0])
    item2 = KeyboardButton(bottons[lang][1])
    item3 = KeyboardButton(bottons[lang][2])
    item4 = KeyboardButton(bottons[lang][3])
    item5 = KeyboardButton(bottons[lang][4])
    item6 = KeyboardButton(bottons[lang][5])
    item7 = KeyboardButton(bottons[lang][6])
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    return markup


def get_phone_number(lang):

    bottons = {'uz': 'Telefon raqamni yuborish',
               'ru': 'Отправить номер телефона'}

    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    item = KeyboardButton(bottons[lang], request_contact=True)
    markup.add(item)
    return markup


def individuals(lang):

    bottons = {'uz' : ['💰Omonatlar', '💳Karta buyurtmasi', '💸Pul o\'tkazmalari', '💼Kreditlar', '📝Tariflar',
                       '📥To\'lov qabul qilish', '📜Jamg‘arma sertifikatlari', '🗄Depozit quticha', '🏠 Bosh menu'],
               'ru' : ['💰Вклады', '💳Оформление карты', '💸Денежные переводы', '💼Кредиты', '📝Тарифы',
                       '📥Прием платежей', '📜Сберегательные сертификаты', '🗄Депозитные ячейки', '🏠 Главное меню']}

    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    item1 = KeyboardButton(bottons[lang][0])
    item2 = KeyboardButton(bottons[lang][1])
    item3 = KeyboardButton(bottons[lang][2])
    item4 = KeyboardButton(bottons[lang][3])
    item5 = KeyboardButton(bottons[lang][4])
    item6 = KeyboardButton(bottons[lang][5])
    item7 = KeyboardButton(bottons[lang][6])
    item8 = KeyboardButton(bottons[lang][7])
    item9 = KeyboardButton(bottons[lang][8])
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
    return markup

def corporate_clients(lang):

    bottons = {'uz': ['📓 Tariflar depozinym hisob', '🗂Hujjat shablonlari', '💼Kreditlar', '🏛Korrespondent banklar',
                      '💲Hujjatli operatsiyalar', '📈Depositlar', '📚Xizmat paketlari', '◀️ Orqaga'],
               'ru': ['📓Тарифы по депозитным счетам', '🗂Шаблоны документов', '💼Кредиты', '🏛Банки-корреспонденты',
                      '💲Документарные операции', '📈Депозиты', '📚Пакеты услуг', '◀️ Назад']}

    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    item1 = KeyboardButton(bottons[lang][0])
    item2 = KeyboardButton(bottons[lang][1])
    item3 = KeyboardButton(bottons[lang][2])
    item4 = KeyboardButton(bottons[lang][3])
    item5 = KeyboardButton(bottons[lang][4])
    item6 = KeyboardButton(bottons[lang][5])
    item7 = KeyboardButton(bottons[lang][6])
    item8 = KeyboardButton(bottons[lang][7])
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    return markup

def map(lang):

    bottons = {'uz': ['Filiallar', 'Bankomatlar', '◀️ Orqaga'],
               'ru': ['Филиалы', 'Банкоматы', '◀️ Назад']}

    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    item1 = KeyboardButton(bottons[lang][0])
    item2 = KeyboardButton(bottons[lang][1])
    item3 = KeyboardButton(bottons[lang][2])
    markup.add(item1, item2, item3)
    return markup

def currancy(lang):

    bottons = {'uz': ['💵 Shu va boshqa kurslar', 'https://www.infinbank.com/uz/private/exchange-rates'],
               'ru': ['-- 💵 Shu va boshqa kurslar --', 'infinbank.com/ru/private/exchange-rates']}

    markup = InlineKeyboardMarkup()
    item1 = InlineKeyboardButton(bottons[lang][0], url = bottons[lang][1])
    markup.add(item1)
    return markup


def language(lang):

    bottons = {'uz': ['🌏 Til', '◀️ Orqaga'],
               'ru': ['🌏 Язык', '◀️ Назад']}

    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    item1 = KeyboardButton(bottons[lang][0])
    item2 = KeyboardButton(bottons[lang][1])
    markup.add(item1, item2)
    return markup
