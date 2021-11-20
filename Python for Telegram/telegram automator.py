import re
from bs4 import BeautifulSoup
import requests
import random
from os import *
API_KEY = '2139603976:AAGO8nMeI_fVNQRVoRRVAb_WrDDT8jmR7II' # This is the API key for connecting to that particular bot in Telegram.

Good_responses =[
  'Ok, That sounds pretty good!!',
  'I am glad to hear that',
  'Awsome, tell me more about it!! 😃',
  'Ooh so, what happened next?',
  'Pretty understandable, time does change everything',
]

Bad_responses =[
  'Oh, that is not good',
  'I am sorry to hear that, things will get better I promise',
  'Oh, I am sorry to hear that',
  'Oh, I know it feels bad 🤕',
  'Don\'t worry, I am here to help you',
  'I am sorry to hear that, I will try to make it better',
]


def sample_responses(inpTxt):
  user_message = str(inpTxt).lower()
  buffer = user_message.replace(' ','+')
  url = 'https://www.google.com/search?q=' + buffer
  if user_message == 'hi' or user_message == 'hello':
    return 'Hello!'
  elif user_message == 'how are you?' or user_message == 'how are you':
    return 'I am fine, thanks!'
  elif user_message == 'what is your name?' or user_message == 'what is your name':
    return 'My name is Automator'
  elif user_message == 'what is your job?' or user_message == 'what is your job':
    return 'I am a bot'
  elif user_message == 'what is your age?' or user_message == 'what is your age':
    return 'I am immortal'

  # Regular Expression...
  elif re.match(r'^[a-zA-Z0-9 ]+\?$', user_message):
  #google search for the user message
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # grab div with aria-level = "3"
    result1 = soup.find_all('div', {"aria-level":"3"})
    print(result1)
    result2 = soup.find_all('span', class_='desktop-title-subcontent')
    if result1[0] == ''and result2[0] == '':
      return 'Sorry, I cannot help you with that, ask one word answer type questions please'
    else:
      return result1[0].text + '\n' + result2[0].text
  else:
    return str(BeautifulSoup(requests.get(url).text, 'html.parser').find_all('div', ariaLevel_ = "3"))

from telegram.ext import *

def start_command(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! I am Automator, ask me anything')

def author(update, context):
  update.message.reply_text('Author: Tanmay Kumar')

def help_command(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text='I can help you with anything, just simply ask questions')

def handle_message(update, context):
  text = str(update.message.text).lower()
  response = sample_responses(text)
  update.message.reply_text(response)

def error(update, context):
  print(f"Error: {context.error}")

def main():
  updater = Updater(API_KEY, use_context=True)
  dp = updater.dispatcher

  dp.add_handler(CommandHandler("start", start_command))
  dp.add_handler(CommandHandler("help", help_command))
  dp.add_handler(CommandHandler("author", author))
  dp.add_handler(MessageHandler(Filters.text, handle_message))
  dp.add_error_handler(error)

  updater.start_polling(2)
  updater.idle()

main() # run the main function