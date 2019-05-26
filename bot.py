from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, ephem

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = str('Вызван /start')
    update.message.reply_text(text)

def planet_position (bot,update):
    user_text = update.message.text.split()
    input_planet = (user_text[1])
    if input_planet == 'Марс':
        update.message.reply_text(ephem.constellation(ephem.Mars('2000/05/26')))
    elif input_planet == 'Юпитер':
        update.message.reply_text(ephem.constellation(ephem.Jupiter('2019/05/26')))


def talk_to_me(bot, update):
    user_text = update.message.text
    update.message.reply_text(f'{user_text}, {update.message.from_user.first_name}')


def main():
    mybot = Updater('883704044:AAEgGQKBqM-5tOQnApLj--n-T7Hhub8OL4w')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', planet_position))
    mybot.start_polling()
    mybot.idle()


main()
