import telebot as tb
import pandas as pd

token = '1915907677:AAGZj_C1WlL3z_vXZctVdQpJ3EJFMFQNgWY' 
bot = tb.TeleBot(token) #инициализация бота по токену

#прописываем, что бот должен делать
@bot.message_handler(content_types=['text']) #регистрируем функцию в боте

def my_name(message):
    if str(message.text).lower() in ['привет', 'hi', 'hello', 'здравствуйте'] or message.text == '/start':
        bot.send_message(message.chat.id, 'Привет! Меня зовут Грандик. Я постараюсь тебе помочь и рассказать про стоимость анализов в клинике "Гранд Медика"')
        bot.send_message(message.chat.id, 'Напишите точное название нужного Вам анализа, а я поищу его в прайсе. Только я еще маленький, поэтому ищу точные совпадения, пожалуйста, не ошибайся ' + u'\U0001F60A')
    else:
        #считываем данные из прайса
        price_data = pd.read_excel('List_analyz.xlsx', sheet_name='data') #считывает данные из файла
        price_dict = price_data.to_dict(orient='records') #преобразовываем данные в словарь Услуга-Цена
        find_price = [] #в этот список будут сохраняться найденные услуги

        for element in price_dict: #ищем нужные анализы по названию
            if str(message.text).lower() in ['ковид', 'covid', 'анализ на ковид', 'анализ на covid']: #инициализация анализов на ковид
                str1 = 'sars-cov-2'
            else:
                str1 = str(message.text).lower()
            str2 = str(element['Service']).lower()
            str3 = str(element['Section']).lower()
            #if set(str(message.text).lower()).issubset(set(str(element['Service']).lower())):
            #if str(message.text).lower() in str(element['Service']).lower():
            if set(str1.split()).issubset(set(str2.split())) or set(str1.split()).issubset(set(str3.split())):
                find_price.append(element['Service'] + ' - ' + str(element['Price']) + ' руб.')
            
        #общаемся, если услугу найти не получается
        if len(find_price) == 0:
            bot.send_message(message.chat.id, 'Что-то я не разобрался... ' + u'\U0001F61E' + ' Позвони, пожалуйста, (3843) 994-994. Но я буду учиться и в следующий раз обязательно справлюсь!')
        else:
            for serv in find_price: #вывод на печать списка с найденными анализами
                bot.send_message(message.chat.id, serv + '\n')

bot.polling(none_stop=True) #метод polling позволяет получать сообщения, "режим ожидания" сообщений
