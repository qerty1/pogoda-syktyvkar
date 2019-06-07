import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = 'ru')
while True:
    place = input('В каком городе хотите узнать погоду?(Напишите "Выход", если хотите закончить): ')

    if place == "Выход":
        break
    else:
        observation = owm.weather_at_place(place)
        w = observation.get_weather()

        temp = w.get_temperature('celsius')["temp"]

        print( "В городе " + place + " сейчас " + w.get_detailed_status())
        print( 'Температура сейчас примерно: ' + str(temp))
print('Завершение')    

