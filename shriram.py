import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from threading import Thread 
from flask import Flask 

# Replace with your bot token from BotFather
BOT_TOKEN = "8142184791:AAEG3Zhefs7HAB-fv7nTKehsXj_AOetaj9Y"

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "I am alive"

def run_http_server():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_http_server)
    t.start()

# Handle all incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Create an inline keyboard with the desired link
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("CREATE YOUR NEW 🆔", url="https://99exch.io/auth/login?to=/")
    markup.add(button)

    # Send the same message with the inline button
    bot.send_message(message.chat.id, message.text, reply_markup=markup)

# Run the bot
keep_alive()
print("Bot is running...")
bot.polling()