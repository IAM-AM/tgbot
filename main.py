import telebot
from telebot import types

bot = telebot.TeleBot('5776265348:AAEriTiHysOU-N5avKJ8496eoUHCrQeckgs')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Hi":
        bot.send_message(message.chat.id, "Hey there!", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "(I don't get it", parse_mode='html')

bot.polling(none_stop=True)
#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardMarkup("Visit a web site", url="https://www.onliner.by/"))
#     bot.send_message(message.chat.id, 'Navigate to the web site', reply_markup=markup)
#
# @bot.message_handler(commands=['help'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     website = types.KeyboardButton('Web Site')
#     start = types.KeyboardButton('Start')
#     markup.add(website, start)
#     bot.send_message(message.chat.id, 'Navigate to the web site', reply_markup=markup)
#
#
