# Python automator for taking CPU and RAM usage Limit and handling it with bot in Telegram and also storing the commands in Database.

from os import *
import pymongo
import psutil, datetime, sys
from pymongo.message import update

API_KEY = '2115103541:AAECPwNj7dHvnK_4ifjoY6wLtGlrviHCdi4' # This is the API key for connecting to that particular bot in Telegram.


client = pymongo.MongoClient("mongodb+srv://TanmayKumar:AP6OlZa09wFSz7nD@cluster0.yi9rj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

if db.get_collection('TelegramAutomator') is None:
  db.create_collection('TelegramAutomator')


# Working functions for different handles of the bot...

from telegram.ext import *
# Default message to other useless messages.
def default_message(update, context):
   update.message.reply_text("Only Command Handles will work for more information type '/help' to know more!!")
  #  No Need to add these messages to the database.


# Task responses
# Help Command
def help_command(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text='Some of the working commands are :'+
  '\n1. /start : used to start the bot'+
  '\n2. /help : used to get the help of the bot'+
  '\n3. /author : used to get the author of the bot'+
  '\n4. /show : used to show the database of the bot'+
  '\n5. /CPU : Tells about the current usage of the CPU for a particular PID'
  '\n6. /RAM : Tells about the current usage of the RAM for a particular PID'
  '\n7. /CPU_Limit : To set the CPU limit for a particular PID' +
  '\n8. /RAM_Limit : To set the RAM limit for a particular PID' +
  '\n9. /Kill : To kill a particular PID' +
  '\n10. /Kill_All_RAM : Kill all the processes above 50% RAM Usage'+
  '\n11. /Kill_All_CPU : Kill all the processes above 50% CPU Usage'+
  '\n12. /History : To show the history of Chats of the bot' +
  '\n13. /pop : To pop the last message of the chat and from the database' +
  '\n14. /pop_all : To pop all the messages of the chat and from the database' +
  '\n15. /pop_all_but_last : To pop all the messages of the chat except the last one and from the database' +
  '\n16. /Status : To give summary of computer.'+
  '\n17. /exit : Closing the program.'
  )
# Start Command
def start_command(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! I am Automator, ask me anything')
  db.TelegramAutomator.insert_one({'Message':'/start', 'Response':'Hello! I am Automator, ask me anything'})

# Author Command
def author(update, context):
  update.message.reply_text('Author: Tanmay Kumar\nMy registeration number is : 19BCE2146')
  db.TelegramAutomator.insert_one({'Message':'/author', 'Response':'Author: Tanmay Kumar\nMy registeration number is : 19BCE2146'})

# Show Command
def show_command(update, context):
  Response = ""
  for i in db.TelegramAutomator.find():
    print(i)
    Response = Response + str(i) + ' \n'
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(i))
  db.TelegramAutomator.insert_one({'Message':'/show', 'Response':Response, 'Time' : datetime.datetime.now()})

# CPU Command
def CPU(update, context):
  pid = str(update.message.text).split(' ')[1]
  if pid == '':
    update.message.reply_text('Please enter the PID')
    db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'Please enter the PID', 'Time' : datetime.datetime.now()})
  else:
    try:
      p = psutil.Process(int(pid))
      update.message.reply_text('CPU Usage for PID ' + str(pid) + ' is ' + str(p.cpu_percent()) + '%')
      db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'CPU Usage for PID ' + str(pid) + ' is ' + str(p.cpu_percent()) + '%', 'Time' : datetime.datetime.now()})
    except:
      update.message.reply_text('PID not found')
      db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'PID not found', 'Time' : datetime.datetime.now()})

# RAM Command
def RAM(update, context):
  pid = str(update.message.text).split(' ')[1]
  if pid == '':
    update.message.reply_text('Please enter the PID')
    db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'Please enter the PID', 'Time' : datetime.datetime.now()})
  else:
    try:
      p = psutil.Process(int(pid))
      update.message.reply_text('RAM Usage for PID ' + str(pid) + ' is ' + str(p.memory_percent()) + '%')
      db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'RAM Usage for PID ' + str(pid) + ' is ' + str(p.memory_percent()) + '%'})
    except:
      update.message.reply_text('PID not found')
      db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'PID not found', 'Time' : datetime.datetime.now()})

# CPU_Limit Command
def CPU_Limit(update, context):
  pid = str(update.message.text).split(' ')[1]
  limit = str(update.message.text).split(' ')[2]
  if pid == '' or limit == '':
    update.message.reply_text('Please enter the PID and the limit')
    db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'Please enter the PID and the limit', 'Time' : datetime.datetime.now()})
  else:
    try:
      p = psutil.Process(int(pid))
      p.cpu_percent(limit)
      update.message.reply_text('CPU Limit for PID ' + str(pid) + ' is ' + str(limit) + '%')
      db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'CPU Limit for PID ' + str(pid) + ' is ' + str(limit) + '%', 'Time' : datetime.datetime.now()})
    except:
      update.message.reply_text('PID not found')
      db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'PID not found', 'Time' : datetime.datetime.now()})

# RAM_Limit Command
def RAM_Limit(update, context):
  pid = str(update.message.text).split(' ')[1]
  limit = str(update.message.text).split(' ')[2]
  if pid == '' or limit == '':
    update.message.reply_text('Please enter the PID and the limit')
    db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'Please enter the PID and the limit', 'Time' : datetime.datetime.now()})
  else:
    try:
      p = psutil.Process(int(pid))
      p.memory_percent(limit)
      update.message.reply_text('RAM Limit for PID ' + str(pid) + ' is ' + str(limit) + '%')
      db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'RAM Limit for PID ' + str(pid) + ' is ' + str(limit) + '%', 'Time' : datetime.datetime.now()})
    except:
      update.message.reply_text('PID not found')
      db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'PID not found', 'Time' : datetime.datetime.now()})

# Kill Command
def Kill(update, context):
  pid = str(update.message.text).split(' ')[1]
  if pid == '':
    update.message.reply_text('Please enter the PID')
    db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'Please enter the PID', 'Time' : datetime.datetime.now()})
  else:
    try:
      p = psutil.Process(int(pid))
      p.kill()
      update.message.reply_text('Killed PID ' + str(pid))
      db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'Killed PID ' + str(pid), 'Time' : datetime.datetime.now()})
    except:
      update.message.reply_text('PID not found')
      db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'PID not found', 'Time' : datetime.datetime.now()})

# Kill_All_CPU Command
def Kill_All_CPU(update, context):
  for proc in psutil.process_iter():
    try:
      p = psutil.Process(proc.pid)
      if p.cpu_percent() > 50:
        p.kill()
        update.message.reply_text('Killed PID ' + str(proc.pid) + ' with CPU Usage ' + str(p.cpu_percent()) + '%')
        db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'Killed PID ' + str(proc.pid) + ' with CPU Usage ' + str(p.cpu_percent()) + '%', 'Time' : datetime.datetime.now()})
    except:
      pass

# Kill_All_RAM Command
def Kill_All_RAM(update, context):
  for proc in psutil.process_iter():
    try:
      p = psutil.Process(proc.pid)
      if p.memory_percent() > 50:
        p.kill()
        update.message.reply_text('Killed PID ' + str(proc.pid) + ' with RAM Usage ' + str(p.memory_percent()) + '%')
        db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'Killed PID ' + str(proc.pid) + ' with RAM Usage ' + str(p.memory_percent()) + '%', 'Time' : datetime.datetime.now()})
    except:
      pass

# Kill_All_CPU_RAM Command
def Kill_All_CPU_RAM(update, context):
  for proc in psutil.process_iter():
    try:
      p = psutil.Process(proc.pid)
      if p.cpu_percent() > 50 or p.memory_percent() > 50:
        p.kill()
        update.message.reply_text('Killed PID ' + str(proc.pid) + ' with CPU Usage ' + str(p.cpu_percent()) + '% and RAM Usage ' + str(p.memory_percent()) + '%')
        db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'Killed PID ' + str(proc.pid) + ' with CPU Usage ' + str(p.cpu_percent()) + '% and RAM Usage ' + str(p.memory_percent()) + '%', 'Time' : datetime.datetime.now()})
    except:
      pass

# History Command
def History(update, context):
  count = str(update.message.text).split(' ')[1]
  try:
    if count == '':
      count = 10
      update.message.reply_text('Showing last ' + str(count) + ' messages')
      db.TelegramAutomator.find().sort('Time', -1).limit(int(count))
      update.message.reply_text(str(db.TelegramAutomator.find().sort('Time', -1).limit(int(count))))
    else:
      update.message.reply_text('Showing last ' + str(count) + ' messages')
      db.TelegramAutomator.find().sort('Time', -1).limit(int(count))
      update.message.reply_text(str(db.TelegramAutomator.find().sort('Time', -1).limit(int(count))))
  except:
    update.message.reply_text('Please enter a valid number')
    db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'Please enter a valid number', 'Time' : datetime.datetime.now()})
  # No Need to insert this I/O inside Database

# pop Command
def pop(update, context):
  try:
    history = db.TelegramAutomator.find({'Chat_ID':str(update.message.chat_id)})
    for i in history:
      db.TelegramAutomator.delete_one({'_id':i['_id']})
  except:
    update.message.reply_text('No History')
  # No Need to insert this I/O inside Database

# pop_all Command
def pop_all(update, context):
  try:
    history = db.TelegramAutomator.find()
    for i in history:
      db.TelegramAutomator.delete_one({'_id':i['_id']})
  except:
    update.message.reply_text('No History')
  # No Need to insert this I/O inside Database

# pop_all_but_last Command
def pop_all_but_last(update, context):
  try:
    history = db.TelegramAutomator.find()
    for i in history:
      if i['_id'] != history[-1]['_id']:
        db.TelegramAutomator.delete_one({'_id':i['_id']})
  except:
    update.message.reply_text('No History')
  # No Need to insert this I/O inside Database

# Status Command
def Status(update, context):
  update.message.reply_text('CPU Usage: ' + str(psutil.cpu_percent()) + '%\nRAM Usage: ' + str(psutil.virtual_memory().percent) + '%')
  db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'CPU Usage: ' + str(psutil.cpu_percent()) + '%\nRAM Usage: ' + str(psutil.virtual_memory().percent) + '%', 'Time' : datetime.datetime.now()})

# Exit Command 
def Exit(update, context):
  update.message.reply_text('Exiting...')
  db.TelegramAutomator.insert_one({'Message':str(update.message.text), 'Response':'Exiting...', 'Time' : datetime.datetime.now()})
  sys.exit()

# If there is any error in the bot, it will be handled here...
def error(update, context):
  print(f"Error: {context.error}")



def main():
  updater = Updater(API_KEY, use_context=True)
  dp = updater.dispatcher
  # All the commands to the bot "Command Handler"
  dp.add_handler(CommandHandler("start", start_command))
  dp.add_handler(CommandHandler("help", help_command))
  dp.add_handler(CommandHandler("author", author))
  dp.add_handler(CommandHandler("show", show_command))
  dp.add_handler(CommandHandler("CPU", CPU))
  dp.add_handler(CommandHandler("RAM", RAM))
  dp.add_handler(CommandHandler("CPU_Limit", CPU_Limit))
  dp.add_handler(CommandHandler("RAM_Limit", RAM_Limit))
  dp.add_handler(CommandHandler("Kill", Kill))
  dp.add_handler(CommandHandler("Kill_All_CPU", Kill_All_CPU))
  dp.add_handler(CommandHandler("Kill_All_RAM", Kill_All_RAM))
  dp.add_handler(CommandHandler("Kill_All_CPU_RAM", Kill_All_CPU_RAM))
  dp.add_handler(CommandHandler("History", History))
  dp.add_handler(CommandHandler("pop", pop))
  dp.add_handler(CommandHandler("pop_all", pop_all))
  dp.add_handler(CommandHandler("pop_all_but_last", pop_all_but_last))
  dp.add_handler(CommandHandler("Status", Status))
  dp.add_handler(CommandHandler("Exit", Exit))

  dp.add_handler(MessageHandler(Filters.text,default_message))
  dp.add_error_handler(error)

  updater.start_polling(2)
  updater.idle()

main() # Running the main function