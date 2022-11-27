#библиотеки, которые загружаем из вне
import telebot
import time
TOKEN = 'Вставь_свой_токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('rat.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Графические файлы")
	item2 = types.KeyboardButton("Видео файлы")
	item3 = types.KeyboardButton("Аудио файлы")
	item4 = types.KeyboardButton("Другое")

	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, "Приветики, {0.first_name}! Меня зовут Рейти!🐭 Я твой маленький помощник для поиска и подготовки файлов для тестирования. Кажется тебе нужна моя помощь в поиске файлов, скажи, что именно тебе необходимо и я постараюсь тебе помочь🐁".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Графические файлы':
			bot.send_message(message.chat.id, 'Хм, сейчас попробую найти🙃')
			bot.send_video(message.chat.id, video=open('sticker1.mp4', 'rb'), supports_streaming=True)
			time.sleep(0.7)
			bot.send_message(message.chat.id, 'Вот, что удалось найти  https://disk.yandex.ru/d/va_Q3OO_QwwWxQ')
		elif message.text == 'Видео файлы':
			bot.send_message(message.chat.id, 'Подожди, сейчас принесу ☺️')
			bot.send_video(message.chat.id, video=open('sticker2.mp4', 'rb'), supports_streaming=True)
			time.sleep(1)
			bot.send_message(message.chat.id, 'Фух, так спешил, что даже немного устал. Держи https://disk.yandex.ru/d/Iq7rrp8iv5kDLw ')
		elif message.text == 'Аудио файлы':
			bot.send_message(message.chat.id, 'По секрету иногда мне даже приходится драться, чтобы принести то, что нужно, но я готов помочь тебе, не смотря ни на что!😅')
			bot.send_video(message.chat.id, video=open('sticker3.mp4', 'rb'), supports_streaming=True)
			time.sleep(3)
			bot.send_message(message.chat.id, 'Вот держи https://disk.yandex.ru/d/bbGzvSgjba7gwg')
		elif message.text == 'Другое':
			bot.send_message(message.chat.id, 'Прости, но я не смог тебе ничем помочь. Напиши, пожалуйста, свои пожелания и отзыв💛 https://t.me/Saymuria.')
		else:
			bot.send_message(message.chat.id, 'Прости, но я не смог тебе ничем помочь. Напиши, пожалуйста, свои пожелания и отзыв💛 https://t.me/Saymuria.')

bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
