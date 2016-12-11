# -*- coding: utf-8 -*-
import config
import telebot
import time
import os
from telebot import types

bot = telebot.TeleBot(config.token)
bot.remove_webhook()

def ping_me():
	hostname = "82.199.120.22"
	response = os.system("ping -c 1 " + hostname)
	#response = os.system("ps -e | grep apache2")

	if response == 0:
		return "Пингуется!"
	else:
		return "Не пингуется!"

def show_messages(message):
	text = "Message - "
	result = text + message
	print(result)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Ты можешь узнать\n/time - время\n/ping - работуспособность моей сети")

@bot.message_handler(commands=['time'])
def get_me(message):
	bot.send_message(message.chat.id, time.asctime())

@bot.message_handler(commands=['ping'])
def get_me(message):
	bot.send_message(message.chat.id, ping_me())

bot.polling()