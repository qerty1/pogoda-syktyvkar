import vk_api
import time
import random
import pyowm
token = 'bd6815e76baac714b41616ba5e399daf506a2242d5295f18fc9791d9e39c9e104ce58ace770ab97339ce6'

vk = vk_api.VkApi(token = token)

vk._auth_token()

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = 'ru')

while True:
    try:
        messages = vk.method('messages.getConversations', {'offset' : 0, 'count': 20, 'filter': "unanswered"})
        if messages['count'] >= 1:
            id = messages['items'][0]['last_message']['from_id']
            body = messages['items'][0]['last_message']['text']
            if body.lower() == 'привет':
                vk.method('messages.send', {'peer_id': id, 'message': 'Привет! я могу показать погоду в Сыктывкаре, напиши "Сыктывкар" или что угодно ', 'random_id': random.randint(1, 2147483647)})
            
            elif body.lower() == 'пока':
                vk.method('messages.send', {'peer_id': id, 'message': 'Пока! Пиши ещё', 'random_id': random.randint(1, 2147483647)})
            elif body.lower() == 'сыктывкар':
                observation = owm.weather_at_place(body)
                w = observation.get_weather()
                temp = w.get_temperature('celsius')["temp"]
                vk.method('messages.send', {'peer_id': id, 'message': 'В городе '+ body + " сейчас " + w.get_detailed_status(), 'random_id': random.randint(1, 2147483647)})
                vk.method('messages.send', {'peer_id': id, 'message': 'Температура сейчас примерно: ' + str(temp), 'random_id': random.randint(1, 2147483647)})
            elif body.lower() == 'я':
                vk.method('messages.send', {'peer_id': id, 'message': 'Да ты красавчик!', 'random_id': random.randint(1, 2147483647)})
                observation = owm.weather_at_place("Сыктывкар")
                w = observation.get_weather()
                temp = w.get_temperature('celsius')["temp"]
                vk.method('messages.send', {'peer_id': id, 'message': "В городе Сыктывкар  сейчас " + w.get_detailed_status(), 'random_id': random.randint(1, 2147483647)})
                vk.method('messages.send', {'peer_id': id, 'message': 'Температура сейчас примерно: ' + str(temp), 'random_id': random.randint(1, 2147483647)})
            else:
                observation = owm.weather_at_place("Сыктывкар")
                w = observation.get_weather()
                temp = w.get_temperature('celsius')["temp"]
                vk.method('messages.send', {'peer_id': id, 'message': "В городе Сыктывкар  сейчас " + w.get_detailed_status(), 'random_id': random.randint(1, 2147483647)})
                vk.method('messages.send', {'peer_id': id, 'message': 'Температура сейчас примерно: ' + str(temp), 'random_id': random.randint(1, 2147483647)})

    except Exception as E:
        time.sleep(1)
