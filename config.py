from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

botToken = "5462513594:AAHU0glmTO16y4ekgynsq3yqG8GtUzv855E"
WEATHER_TOKEN = 'e7e5955c215fef21ed5fea9cf17ebc68'

bot = Bot(token=botToken)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())