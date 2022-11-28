#WheatherMap
import pyowm

owm = pyowm.OWM('21e7b541630f7408893719545941292a', language = "ru" )

Place = input("В каком городе/стране вы сейчас находитесь?: ")

observation = owm.weather_at_place(Place)

w = observation.get_weather()

temp = w.get_temperature("celsius")["temp"]

print("Сейчас в " + Place + " " + w.get_detailed_status())

print("Сейчас температура:" + str(temp))

if temp < 10:
	print("Холодноб оденься по теплее!")
elif temp < 20:
	print("Не так холодно, но всё равно оденься!")
elif temp > 20:
	print("Снаруже тепло, иди гуляй!")
else: Print("Такой город не сушествует!")