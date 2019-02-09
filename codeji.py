import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

bot=telegram.Bot('789983548:AAEfx_bx9rJlETIJN8CGdabqhmXY2j1uSFI')
updater=Updater(token='789983548:AAEfx_bx9rJlETIJN8CGdabqhmXY2j1uSFI')
dispatcher=updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger=logging.getLogger(__name__)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello and Welcome!! This bot will introduce you the basics of computer languages and programming")
    menu_keyboard=[['/python'],['/c']]
    menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True) 
    bot.send_message(chat_id=update.message.chat_id, text="Select what language you'd like to know more about:\n1.Python\n2.C", reply_markup=menu_markup)         
start_handler=CommandHandler('start',start)
dispatcher.add_handler(start_handler)

def python(bot, update):
    menu_keyboard=[['/intro'],['/commands'],['/start']]
    menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True) 
    bot.send_message(chat_id=update.message.chat_id, text="Select which topic to browse:\n\n1.Introduction\n2.Commands", reply_markup=menu_markup)
    
    def intro(bot,update):
        menu_keyboard=[['/python']]  
        menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
        bot.send_message(chat_id=update.message.chat_id, text="Python is a widely used general-purpose, high level programming language. It was initially designed by Guido van Rossum in 1991 and developed by Python Software Foundation. It was mainly developed for emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code.Python is a programming language that lets you work quickly and integrate systems more efficiently.",reply_markup=menu_markup)
    pyintro_handler=CommandHandler('intro',intro)
    dispatcher.add_handler(pyintro_handler)  
    
    def commands(bot,update):
        menu_keyboard=[['/print'],['/comments'],['/string'],['/lists'],['/python']]
        menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
        bot.send_message(chat_id=update.message.chat_id, text="1.Print\n2.Comments\n3.String Manipulations\n4.List\n5.Tuples\n6.Sets\n7.Dictionary",reply_markup=menu_markup)
    
        def print(bot,update):
            menu_keyboard=[['/commands']] 
            menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
            bot.send_message(chat_id=update.message.chat_id, text="The print command is used to display a piece of text on the screen")
            bot.send_message(chat_id=update.message.chat_id, text="Syntax : print('<required text>')")
            bot.send_message(chat_id=update.message.chat_id, text="Example:\n\nprint('Hello World')\nOutput:Hello World",reply_markup=menu_markup)
        cmdprint_handler=CommandHandler("print",print)
        dispatcher.add_handler(cmdprint_handler)

        def comments(bot,update):
            menu_keyboard=[['/commands']] 
            menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
            bot.send_message(chat_id=update.message.chat_id, text="Used to comment a line. Commented lines are ignored during compilation. They are used mainly for documentation purposes.")
            bot.send_message(chat_id=update.message.chat_id, text="Syntax : #<any line in the program>")
            bot.send_message(chat_id=update.message.chat_id, text="Example: #print('Hello')",reply_markup=menu_markup)
        cmdcmt_handler=CommandHandler("comments",comments)
        dispatcher.add_handler(cmdcmt_handler)

        def string(bot,update):
            menu_keyboard=[['/commands']] 
            menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
            bot.send_message(chat_id=update.message.chat_id, text="Getting a single letter from a string\nEg:\na='Hello'\nprint(a[1])\nOutput: e")
            bot.send_message(chat_id=update.message.chat_id, text="Getting a substring from a string\nEg:\na='Hello'\nprint(a[1:3])\nOutput: ll")
            bot.send_message(chat_id=update.message.chat_id, text="Getting lenght of a string\nEg:\na='Hello'\nprint(len(a))\nOutput:5",reply_markup=menu_markup)    
        cmdstr_handler=CommandHandler("string",string)
        dispatcher.add_handler(cmdstr_handler)

        def lists(bot,update):
            menu_keyboard=[['/commands']] 
            menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
            bot.send_message(chat_id=update.message.chat_id, text="A list is a collection which is ordered and changeable. In Python lists are written with square brackets.")
            bot.send_message(chat_id=update.message.chat_id, text="Syntax : <list-name>=['value1','value2'.....'value n']")
            bot.send_message(chat_id=update.message.chat_id, text="Example:\n\nlist=['bat','cat','mat']")
            bot.send_message(chat_id=update.message.chat_id, text="Accessing a list\nEng:\nlist=['bat','cat','mat']\nprint(list[2])\nOutput:mat",reply_markup=menu_markup)    
        cmdlist_handler=CommandHandler("lists",lists)
        dispatcher.add_handler(cmdlist_handler)

    pycmd_handler=CommandHandler('commands',commands)
    dispatcher.add_handler(pycmd_handler)

py_handler=CommandHandler('python',python)
dispatcher.add_handler(py_handler)

def c(bot, update):
    menu_keyboard=[['/intro'],['/commands'],['/start']]
    menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id, text="Select which topic to browse:\n\n1.Introduction\n2.Commands", reply_markup=menu_markup)

    def intro(bot,update):
        menu_keyboard=[['/c']]
        menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
        bot.send_message(chat_id=update.message.chat_id, text="C is a procedural programming language. It was initially developed by Dennis Ritchie between 1969 and 1973. It was mainly developed as a system programming language to write operating system. The main features of C language include low-level access to memory, simple set of keywords, and clean style, these features make C language suitable for system programming like operating system or compiler development.",reply_markup=menu_markup)
    cintro_handler=CommandHandler('intro',intro)
    dispatcher.add_handler(cintro_handler)

    def commands(bot, update):
        menu_keyboard=[['/input'],['/output'],['/loops'],['/c']]
        menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
        bot.send_message(chat_id=update.message.chat_id, text="1.Input Functions\n2.Output Function\n3.Loops", reply_markup=menu_markup)
        
        def input(bot,update):
            menu_keyboard=[['/commands']]
            menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
            bot.send_message(chat_id=update.message.chat_id, text="One of the easiest way to take input is using the getchar function. The other way is to use the scanf() function.")
            bot.send_message(chat_id=update.message.chat_id, text="Syntax: \nGetchar :\nvar_name=getchar()\n\nScanf:\nscanf('&format specifier',<variablename>)")
            bot.send_message(chat_id=update.message.chat_id, text="Eg:\n #include<stdio.h>\nvoid main()\n{\nchar title;\ntitle=getchar();\n\nscanf:\nscanf('c',&title)", reply_markup=menu_markup)
        cmdinp_handler=CommandHandler("input",input)
        dispatcher.add_handler(cmdinp_handler)

        def output(bot,update):
            menu_keyboard=[['/commands']]
            menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
            bot.send_message(chat_id=update.message.chat_id, text="To print the output of a variable we use the prinf() function")
            bot.send_message(chat_id=update.message.chat_id, text="Syntax: printf('text with variable',variable names)")
            bot.send_message(chat_id=update.message.chat_id, text="Eg:\n#include<stdio.h>\nvoid main()\n{\int title;\nprintf('d',title)\n}",reply_markup=menu_markup)
        cmdop_handler=CommandHandler("output",output)
        dispatcher.add_handler(cmdop_handler)

        def loops(bot,update):
            menu_keyboard=[['/forl'],['/whilel'],['/dowhile'],['/commands']]  
            menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
            bot.send_message(chat_id=update.message.chat_id, text="Loops are used in programming to repeat a set of instruction until a certain condition is met.")
            bot.send_message(chat_id=update.message.chat_id, text="There are three kinds of loop available in C :\n1.For loop\n2.While loop\n3.Do while loop")
            bot.send_message(chat_id=update.message.chat_id, text="Select which loop :",reply_markup=menu_markup)
            
            def forl(bot,update):
                menu_keyboard=[['/loops']]
                menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
                bot.send_message(chat_id=update.message.chat_id, text="Syntax:\nfor(initialization; testExpression, updateStatement)\n{\n//program code\n}")
                bot.send_message(chat_id=update.message.chat_id, text="The working of this loop is that the initial statement is executed once and then the test expression is evalutated. If the expression is false, the loop is terminted. Else if it is true, the statements inside the loop is repeated until the test expression becomes false.",reply_markup=menu_markup)
            loopfor_handler=CommandHandler("forl",forl)
            dispatcher.add_handler(loopfor_handler)

            def whilel(bot,update):
                menu_keyboard=[['/loops']]
                menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
                bot.send_message(chat_id=update.message.chat_id, text="Syntax:\nwhile(testExpression)\n{\n//program code\n}")
                bot.send_message(chat_id=update.message.chat_id, text="In the while loop the test expression is evaluated and if it is found is true, then the code inside the loop is executed and is continued till the test expression becomes false. If it is false, the whole code is skipped.",reply_markup=menu_markup)
            loopwhile_handler=CommandHandler("whilel",whilel)
            dispatcher.add_handler(loopwhile_handler)

            def dowhile(bot,update):
                menu_keyboard=[['/loops']]
                menu_markup=ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
                bot.send_message(chat_id=update.message.chat_id, text="Syntax:\ndo\n{\n//program code\n}\nwhile(test expression)")
                bot.send_message(chat_id=update.message.chat_id, text="The code inside the loop is executed once. Then the test expression is evaluated. If the value is found to be true the loop continues else the loop is skipped",reply_markup=menu_markup)
            loopdo_handler=CommandHandler("dowhile",dowhile)
            dispatcher.add_handler(loopdo_handler)
            
        cmdloop_handler=CommandHandler("loops",loops)
        dispatcher.add_handler(cmdloop_handler)
    
    ccmd_handler=CommandHandler("commands",commands)
    dispatcher.add_handler(ccmd_handler)

c_handler=CommandHandler('c',c)
dispatcher.add_handler(c_handler)

updater.start_polling()
