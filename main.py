import telebot
import re

bot = telebot.TeleBot('1972648575:AAF8wUxIkweuohWKMmU6t9FWaIzdJ9IKPjM')

@bot.message_handler(content_types=['text'])
def start_command(message):
    command = re.match(r'\/send', message.text)
    theme = re.search(r'-s[^-]*', message.text)
    text = re.search(r'-t[^-]*', message.text)
    mail_list = re.search(r'-m[^-]*', message.text)

    if (theme == None or text == None or mail_list == None):
        return

    theme = re.sub(r'-s\s*', '', theme.group())
    text = re.sub(r'-t\s*', '', text.group())
    mail_list = re.sub(r'-m\s*', '', mail_list.group())
    mail_list = re.findall(r'\w+@\w+\.\w+', mail_list)

    if(command != None):
        if command.group() == '/send':
            bot.send_message(message.chat.id, theme)
            bot.send_message(message.chat.id, text)
            bot.send_message(message.chat.id, mail_list[0])

bot.polling()