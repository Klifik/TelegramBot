import telebot
from telebot import types


token = '5581283557:AAGJibdTtVaYsF2DuXxvuYnWPNhfFGqlXpg'
bot = telebot.TeleBot(token)

#Отрисовка

def gen_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Плоскорезы", callback_data="Плоскорезы")
    item2 = types.InlineKeyboardButton("Садовые товары", callback_data="Садовые товары")
    item3 = types.InlineKeyboardButton("Контакты", callback_data="Контакты")
    markup.add(item1, item2)
    markup.add(item3)
    return markup
@bot.message_handler(commands=['start'])
def message_handler(message):
    from config import URL1
    global user
    user = message.chat.first_name
    bot.send_message(message.chat.id,
                     f' Добро пожаловать в магазин садовых товаров Судогодоское!')
    bot.send_photo(message.chat.id, URL1, reply_markup=gen_markup())
    global idmessage
    idmessage = message.message_id

#Садовые товары
def sadmarkup1():
    markup = types.InlineKeyboardMarkup(row_width=2)
    sp = ['Душ "Степ"', 'Садовый бордюр 100мм', 'Дорожка садовая', 'Наколенники', 'Кустодержатель',
          'Фруктосборник', 'Пугало-Антикрот', 'Сушилка', 'Стул садовый', 'Скворечник', ]
    buttons = []
    c = 0
    next = types.InlineKeyboardButton('Следущяя страница', callback_data='NextSec')
    gv = types.InlineKeyboardButton('Главное меню', callback_data= 'gv')
    for i in range(10):
        item = types.InlineKeyboardButton(sp[i], callback_data=sp[i])
        markup.add(item)
    markup.add(gv, next)
    return markup
def sadmarkup2():
    markup = types.InlineKeyboardMarkup(row_width=2)
    sp = ['Набор для комнатный растений', 'Комби',
          'Туннельный парник (Парник укрытие)']
    buttons = []
    c = 0
    next = types.InlineKeyboardButton('Предыдущая страница', callback_data='BackSec')
    gv = types.InlineKeyboardButton('Главное меню', callback_data= 'gv')
    for i in range(3):
        item = types.InlineKeyboardButton(sp[i], callback_data=sp[i])
        markup.add(item)
    markup.add(gv, next)
    return markup



#Плоскорезы
def plockmarkup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    sp = ['Фокина большой', 'Фокина малый', 'Аист', 'Стриж большой', 'Стриж средний', 'Стриж малый',
          'Стриж укороченный',
          'Корнеудалитель', 'Краб большой', 'Краб малый']
    buttons = []
    c = 0
    next = types.InlineKeyboardButton('Следущяя страница', callback_data='Next')
    gv = types.InlineKeyboardButton('Главное меню', callback_data= 'gv')
    for i in range(10):
        item = types.InlineKeyboardButton(sp[i], callback_data=sp[i])
        markup.add(item)
    markup.add(gv, next)
    return markup
def plockmarkup2():
    markup = types.InlineKeyboardMarkup(row_width=2)
    sp2 = ['Дракон', 'Лепесток', 'Трансформер БВГК', 'Почвообрабатывающий агрегат Чибис',
           'Гидра', 'Тяпка (мотыжка)', 'Плоскорез Z3', 'Плоскорез Z4', 'Аэратор', 'Семейный']
    buttons = []
    c = 0
    next = types.InlineKeyboardButton('Предыдущяя страница', callback_data='Back')
    gv = types.InlineKeyboardButton('Главное меню', callback_data='gv')
    for i in range(10):
        item = types.InlineKeyboardButton(sp2[i], callback_data=sp2[i])
        markup.add(item)
    markup.add(gv, next)
    return markup
def object1(URL):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton('Купить', callback_data='buy')
    back2 = types.InlineKeyboardButton('Назад', callback_data='back1')
    url = types.InlineKeyboardButton('Подробная информация', url=URL)
    markup.add(buy, back2, url)
    return markup
def object2(URL):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton('Купить', callback_data='buy')
    back2 = types.InlineKeyboardButton('Назад', callback_data='back2')
    url = types.InlineKeyboardButton('Подробная информация', url=URL)
    markup.add(buy, back2, url)
    return markup
def object3(URL):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton('Купить', callback_data='buy')
    back2 = types.InlineKeyboardButton('Назад', callback_data='back3')
    url = types.InlineKeyboardButton('Подробная информация', url=URL)
    markup.add(buy, back2, url)
    return markup
def object4(URL):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton('Купить', callback_data='buy')
    back2 = types.InlineKeyboardButton('Назад', callback_data='back4')
    url = types.InlineKeyboardButton('Подробная информация', url=URL)
    markup.add(buy, back2, url)
    return markup
#Обработка
@bot.callback_query_handler(func=lambda call: True)
def reload(call):
    from config import sp1, sp2, sp3, sp4
    if call.data == 'Плоскорезы':
        plock(call.message)
    if call.data == 'Next':
        next(call.message)
    if call.data == 'Back':
        back(call.message)
    if call.data == 'gv':
        gv(call.message)
    for i in range(10):
        if call.data == sp1[i]:
            iter = i
            obj1(call.message, iter)
    for i in range(10):
        if call.data == sp2[i]:
            iter = i
            obj2(call.message, iter)
    if call.data == 'back1':
        back1(call.message)
    if call.data == 'back2':
        back2(call.message)
    if call.data == 'back3':
        back3(call.message)
    if call.data == 'back4':
        back4(call.message)
    if call.data == 'Контакты':
        contakts(call.message)




    if call.data == 'Садовые товары':
        sad(call.message)
    if call.data == 'NextSec':
        NextSec(call.message)
    if call.data == 'BackSec':
        BackSec(call.message)
    for i in range(10):
        if call.data == sp3[i]:
            iter = i
            obj3(call.message, iter)
    for i in range(3):
        if call.data == sp4[i]:
            iter = i
            obj4(call.message, iter)

def contakts(message):
    bot.send_message(message.chat.id, 'Наш адрес: 601351, Владимирская обл.,г.Судогда,ул. Гагарина, 5.\n'
                                      'Наши телефоны: 8(49235)2-12-16; 2-25-12;\n'
                                      'E-mail: srtp@bk.ru; s-ploskorez@gmail.com')
def gv(message):
    from config import URL1
    bot.send_message(message.chat.id,
                     f' Добро пожаловать в магазин садовых товаров Судогодоское!')
    bot.send_photo(message.chat.id, URL1, reply_markup=gen_markup())
    bot.delete_message(message.chat.id, message_id=message.message_id)


#Садовые товары
def sad(message):
    from config import URL2
    bot.send_photo(message.chat.id, URL2, reply_markup=sadmarkup1())
    bot.delete_message(message.chat.id, message_id=message.message_id)
    bot.delete_message(message.chat.id, message_id=message.message_id-1)
def NextSec(message):
    from config import URL2
    bot.send_photo(message.chat.id, URL2, reply_markup=sadmarkup2())
    bot.delete_message(message.chat.id, message_id=message.message_id)
def BackSec(message):
    from config import URL2
    bot.send_photo(message.chat.id, URL2, reply_markup=sadmarkup1())
    bot.delete_message(message.chat.id, message_id=message.message_id)
def obj3(message, i):
    from config import ALLTEXT3, ALLURLINF3, ALLURLPIC3
    bot.send_photo(message.chat.id, ALLURLPIC3[i], caption=ALLTEXT3[i], reply_markup=object3(ALLURLINF3[i]))
    bot.delete_message(message.chat.id, message_id=message.message_id)
def back3(message):
    from config import URL2
    bot.send_photo(message.chat.id, URL2, reply_markup=sadmarkup1())
    bot.delete_message(message.chat.id, message_id=message.message_id)
def back4(message):
    from config import URL2
    bot.send_photo(message.chat.id, URL2, reply_markup=sadmarkup2())
    bot.delete_message(message.chat.id, message_id=message.message_id)
def obj4(message, i):
    from config import ALLTEXT4, ALLURLINF4, ALLURLPIC4
    bot.send_photo(message.chat.id, ALLURLPIC4[i], caption=ALLTEXT4[i], reply_markup=object4(ALLURLINF4[i]))
    bot.delete_message(message.chat.id, message_id=message.message_id)
#Плоскорезы
def plock(message):
    from config import URL2
    bot.send_photo(message.chat.id, URL2, reply_markup=plockmarkup())
    bot.delete_message(message.chat.id, message_id=message.message_id)
    bot.delete_message(message.chat.id, message_id=message.message_id-1)
def next(message):
    from config import URL2
    bot.send_photo(message.chat.id, URL2, reply_markup=plockmarkup2())
    bot.delete_message(message.chat.id, message_id=message.message_id)
def back1(message):
    from config import URL2
    bot.send_photo(message.chat.id, URL2, reply_markup=plockmarkup())
    bot.delete_message(message.chat.id, message_id=message.message_id)
def obj1(message, i):
    from config import ALLTEXT1, ALLURLINF1, ALLURLPIC1
    bot.send_photo(message.chat.id, ALLURLPIC1[i], caption=ALLTEXT1[i], reply_markup=object1(ALLURLINF1[i]))
    bot.delete_message(message.chat.id, message_id=message.message_id)
def obj2(message, i):
    from config import ALLTEXT2, ALLURLINF2, ALLURLPIC2
    bot.send_photo(message.chat.id, ALLURLPIC2[i], caption=ALLTEXT2[i], reply_markup=object2(ALLURLINF2[i]))
    bot.delete_message(message.chat.id, message_id=message.message_id)
def back2(message):
    from config import URL2
    bot.send_photo(message.chat.id, URL2, reply_markup=plockmarkup2())
    bot.delete_message(message.chat.id, message_id=message.message_id)




bot.infinity_polling()
