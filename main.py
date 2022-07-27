
from aiogram import executor,types
from config import dp,WEATHER_TOKEN
import logging
from aiogram.dispatcher import FSMContext
from states import States
import requests

from pprint import pprint

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='weather')
async def weather(msg = types.Message): 
   await msg.reply("Hello where do you live")

@dp.message_handler(content_types="text")
async def getWeather(msg: types.Message):
    userAnswer = msg.text
    link =  f"http://api.openweathermap.org/data/2.5/weather?q={userAnswer}&lang=en&appid={WEATHER_TOKEN}&units=metric" 
    req = requests.get(link).json()
    namecity= req['name']
    temp=req['main']['temp']
    weth = req['weather'][0]['description']
    await msg.reply(text = f'{temp},{namecity},{weth}')

if __name__ == "__main__":
   executor.start_polling(dp,skip_updates=True)
