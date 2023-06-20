import telebot

TOKEN = '6173669360:AAFKquWKqVAydOF2jjix4o3R2Vq3UPA8cd4'

bot = telebot.TeleBot(TOKEN)

keys = {
    'евро' : 'EUR',
    'доллар' : 'USD',
    'рубли' : 'RYB'
}
@bot.message_handler(commands=['start', 'help'])
def help(message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> ' \
           '<в какую валюту перевести>' \
           '<количество переводимой валюты>' \
           '\nУвидеть список доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


bot.polling()