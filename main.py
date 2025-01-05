import os
import telebot

# Тестовый бот 7829240892:AAGTdtDQ_Jw5eJuQ9MKo8uQNDEeyJJgn3xQ
# Продакшн бот
TOKEN = "7829240892:AAGTdtDQ_Jw5eJuQ9MKo8uQNDEeyJJgn3xQ"  # Введите сюда токен своего Telegram-бота
bot = telebot.TeleBot(TOKEN)
bot.set_webhook()
directory = os.path.dirname(__file__)

menu_commands = {

}

commands = {

}

chat_commands = {

}

queries = {

}


@bot.message_handler(content_types=["text"])
def t1(message):
    command = message.text.split()[0]
    if command == '/help':
        return
    if message.chat.type == "private":
        pass
    elif message.chat.type == "group" or message.chat.type == "supergroup":
        pass



@bot.callback_query_handler(func=lambda call: call.data)
def q1(call):
    pass


bot.infinity_polling(timeout=10, long_polling_timeout=5)
