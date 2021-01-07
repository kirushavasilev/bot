import os
import sys
import telebot
import config
import random
import sqlite3


from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	
	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🎲 Рандом от 1 до 10")
	item2 = types.KeyboardButton("🎲 Рандом от 1 до 100")
	item3 = types.KeyboardButton("😔 Как тебе помочь?")
	item4 = types.KeyboardButton("😊 Как дела?")
	item5 = types.KeyboardButton("🌧 Погода")
   

	markup.add(item1, item2, item3, item4, item5)

	bot.send_message(message.chat.id, "Добро времени суток, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный величайшим Nice_KLart! ".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🎲 Рандом от 1 до 100':
			bot.send_message(message.chat.id, str(random.randint(1,100)))
		elif message.text == '😊 Как дела?':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Отлично", callback_data='good')
			item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
		


		elif message.text == '😔 Как тебе помочь?':
			bot.send_message(message.chat.id, 'Напиши Кирюше, что добавить в список моих функций, это лучшая помощь для него на данном этапе ❤ ')
		
		elif message.text == '🌧 Погода':
		    bot.send_message(message.chat.id, 'Не так шустро, я только работаю над этим 😆')

		elif message.text == 'Привет':
		 bot.send_message(message.chat.id, 'Доброго времени суток! Я - Киборг Истребитель, бот созданный величайшим Nice_Klart!')
		
		else:
			bot.send_message(message.chat.id, 'Кажется такой команды не существует 😐')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'Не грустите! Ведь я вас люблю!💖')


	except Exception as e:
		print(repr(e))


# RUN
bot.polling(none_stop=True)