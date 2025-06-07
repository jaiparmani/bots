
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'



# myapp/views.py
import os
import json
import google.generativeai as genai
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Update
from telegram.ext import Application, ContextTypes
from telegram.ext._utils.types import BD


# Telegram bot token
import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from secrets import GEMINI_API_KEY, TELEGRAM_BOT_KEY
# CONFIG
API_KEY = GEMINI_API_KEY
bottoken = TELEGRAM_BOT_KEY
TELEGRAM_BOT_TOKEN = bottoken
GEMINI_API_KEY = API_KEY
# Gemini setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Init Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your Gemini-powered bot. Ask me anything!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    await update.message.chat.send_action(action="typing")

    try:
        response = model.generate_content(user_input)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("Something went wrong: " + str(e))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()