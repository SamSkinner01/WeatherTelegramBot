import telebot
import weather as w
import key as k

API = k.get_telegram_api()

bot = telebot.TeleBot(API)


@bot.message_handler(regexp="weather")
def handle_message(message):
    temperature = w.get_weather()
    bot.send_message(message.chat.id, "Hello! The weather today is:\nMin Temp: " + str(temperature[0]) + "\nMax Temp: " + str(temperature[1]))


# Constantly checking for user input
bot.infinity_polling()

