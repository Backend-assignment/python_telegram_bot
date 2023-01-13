from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup
import os

# get token from env
TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    # get chat_id
    chat_id = update.message.chat.id
    # send welcome message
    bot = context.bot
    bot.sendMessage(chat_id,'Assalom alaykum xush kelibsiz botimizga 👍')

def echo(update: Update, context: CallbackContext):
    pass

def hi(update: Update, context: CallbackContext):
    pass

def help(update: Update, context: CallbackContext):
    pass


updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('help',help))
updater.dispatcher.add_handler(MessageHandler(Filters.text('hi'),hi))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()