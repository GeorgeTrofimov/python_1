import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot("5670633455:AAGT69BfD-NhB97BLDmxK4K2d-IC9CKWzis")

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.first_name) + ',\n/start - запуск бота\n/help - команды бота\nЧтобы узнать погоду напишите в чат название города')

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, '/start - запуск бота\n/help - команды бота\nЧтобы узнать погоду напишите в чат название города')

@bot.message_handler(content_types=['text'])
def test(message):
	try:
		place = message.text

		config_dict = get_default_config()
		config_dict['language'] = 'ru'

		owm = OWM('a7d32c126bd5f821a70268be19ab662e', config_dict)
		mgr = owm.weather_manager()
		observation = mgr.weather_at_place(place)
		w = observation.weather

		t = w.temperature("celsius")
		t1 = t['temp']
		t2 = t['feels_like']
		t3 = t['temp_max']
		t4 = t['temp_min']

		wi = w.wind()['speed']
		humi = w.humidity
		cl = w.clouds
		st = w.status
		dt = w.detailed_status
		ti = w.reference_time('iso')
		pr = w.pressure['press']
		vd = w.visibility_distance

		bot.send_message(message.chat.id, "В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
				"Максимальная температура " + str(t3) + " °C" +"\n" + 
				"Минимальная температура " + str(t4) + " °C" + "\n" + 
				"Ощущается как" + str(t2) + " °C" + "\n" +
				"Скорость ветра " + str(wi) + " м/с" + "\n" + 
				"Давление " + str(pr) + " гПа" + "\n" + 
				"Влажность " + str(humi) + " %" + "\n" + 
				"Видимость " + str(vd) + "  метров" + "\n" +
				"Описание " + str(st) + "\n\n" + str(dt))

	except:
		bot.send_message(message.chat.id,"Такой город не найден!")
		print(str(message.text),"- Не найден")

bot.polling(none_stop=True, interval=0)