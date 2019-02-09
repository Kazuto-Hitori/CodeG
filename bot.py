import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

bot=telegram.Bot('789983548:AAEfx_bx9rJlETIJN8CGdabqhmXY2j1uSFI')

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger=logging.getLogger(__name__)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello and Welcome!! This bot will introduce you the basics of computer languages and programming")
    #bot.send_message(chat_id=update.message.chat_id, text="Select what language you'd like to know more about:\n1./Python\n2./C")
    menu_keyboard=[['/python'],['/c']]
    menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True) 
    bot.send_message(chat_id=update.message.chat_id, text="Select what language you'd like to know more about:\n1./Python\n2./C", reply_markup=menu_markup)         


def python(bot, update):
    keyboard=[[InlineKeyboardButton("Previous",callback_data='1')],[InlineKeyboardButton("Next",callback_data='2')]]
    reply_markup=InlineKeyboardMarkup(keyboard)
    menu_keyboard=[['/introduction'],['/commands']]
    menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
#    def introduction(bot,update)
 #     bot.send_message(chat_id=update.message.chat_id, text)
 #     bot.send_message(chat_id=update.message.chat_id, text="", reply_markup=reply_markup)
def button(bot, update):
    query=update.callback_query
    bot.edit_message_text(text="It's used for for:\n1.Web Development\n2.Software Development\n3.Mathematics\n4.System Scripting", chat_id=query.message.chat_id, message_id=query.message.message_id)
    keyboard=[[InlineKeyboardButton("Previous",callback_data='1')],[InlineKeyboardButton("Next",callback_data='2')]]

        
def main():
  updater=Updater(token='789983548:AAEfx_bx9rJlETIJN8CGdabqhmXY2j1uSFI')
  dispatcher=updater.dispatcher
  start_handler=CommandHandler('start',start)
  dispatcher.add_handler(start_handler)
  py_handler=CommandHandler('python',python)
  dispatcher.add_handler(py_handler)
  updater.dispatcher.add_handler(CallbackQueryHandler(button))
  updater.start_polling()

if __name__ == '__main__':
  main()
