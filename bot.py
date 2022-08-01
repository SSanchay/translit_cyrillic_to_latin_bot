import os
import logging

from aiogram import Bot, Dispatcher, executor, types

#from config import TOKEN

logging.basicConfig(filename='bot.log', encoding = 'utf-8', level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) ## decorator
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Hello, {user_name}!"

    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply(text)

@dp.message_handler()   ## decorator
async def send_translit(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = ''
    lat_decode = {'А': 'A', 'Б': 'B', 'В': 'V',
            'Г': 'G', 'Д': 'D', 'Е': 'E',
            'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
            'И': 'I', 'Й': 'I', 'К': 'K',
            'Л': 'L', 'М': 'M', 'Н': 'N',
            'О': 'O', 'П': 'P', 'Р': 'R',
            'С': 'S', 'Т': 'T', 'У': 'U',
            'Ф': 'F', 'Х': 'KH', 'Ц': 'TS',
            'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
            'Ы': 'Y', 'Ъ': 'IE', 'Э': 'E',
            'Ю': 'IU','Я': 'IA'}
            
    for i in message.text.upper():
        if i in lat_decode:
            text = ''.join((text, lat_decode[i]))
        elif i == ' ':
            text = ''.join((text, i))
        elif i  == 'Ь':
            pass
        else:
            await bot.send_message(user_id, f'Неподходящий символ: {i}!')


    logging.info(f"{user_name=} {user_id=} sent message: {text}")
    await bot.send_message(user_id, text)
    #await bot.send_message(admin_id, text)



if __name__ == '__main__':
    executor.start_polling(dp)