# -*- coding: utf-8 -*-
import config
import telebot
import time
import os
from telebot import types

bot = telebot.TeleBot(config.token)
bot.remove_webhook()

def ping_me():
	hostname = "YOUR IP OR SERVER"
	response = os.system("ping -c 1 " + hostname)
	#response = os.system("ps -e | grep apache2")

	if response == 0:
		return "Пингуется!"
	else:
		return "Не пингуется!"

def show_messages(message):
	text = "Message - "
	result = text + message
	return(result)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Ты можешь узнать\n/time - время\n/ping - работуспособность моей сети")

@bot.message_handler(commands=['time'])
def get_me(message):
	bot.send_message(message.chat.id, time.asctime())

@bot.message_handler(commands=['ping'])
def get_me(message):
	bot.send_message(message.chat.id, ping_me())

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):	
    bot.send_message(message.chat.id, show_messages(message.text))

bot.polling()
