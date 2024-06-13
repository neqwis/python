from aiogram import types,executor,Bot,Dispatcher
from req import send_answer


API = '7138861732:AAEUk88b4d8HTxOpNU5NRi3MWLdyEasF-7c'
bot = Bot(token=API)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def say_hi(message:types.Message):
    user = message.from_user.first_name
    await message.answer('напишите нам свой вопрос')

@dp.message_handler()
async def save(message:types.Message):
    answer = await send_answer(message.text)
    await message.answer(answer)

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
