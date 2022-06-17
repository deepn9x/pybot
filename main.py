from distutils.util import execute
import imp
import ssl
from time import sleep
from xmlrpc.client import Boolean
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import aiohttp
import json

#from telegram import ReplyKeyboardRemove
from db import Database
import markup as nav

# tokenOld='5315163231:AAHgp23m6BxpWDJbmL1RYUnu3bIW_4gW5Zg' 
#token='5456922852:AAFiLYVEqH6iI82TugailS7OVW6DPz9kLn8'
token = '5351233076:AAE2I51jWb3eQTayIRTe3KiZo2-vWkVjmCQ'


bot = Bot(token=token)
dp = Dispatcher(bot)

db = Database('akim.db')

cats = ['Вопросы обеспечения жильём', 
'Вопросы трудоустройства и социального обеспечения',
'Вопросы коммунального хозяйства',
'Вопросы образования',
'Вопросы здравоохранения',
'О вопросах предпринимательства',
'Вопросы сельского хозяйства',
'Земельные вопросы',
'Факты ненадлежащего использования служебного положения',
'Соблюдение законодательной и правовой дисциплины',
'О других вопросах'
]

# @dp.message_handler(content_types=["new_chat_members"])
# async def handler_new_member(message):
#     user_name = message.new_chat_member.first_name
#     await bot.send_message(message.chat.id, "Добро пожаловать, {0}!".format(user_name))

# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await bot.send_message(message.from_user.id, "💁🏻‍♀️📝\nДауыс беретін учаскеңізді табу үшін өзіңіздің ЖСН-іңізді (жеке сәйкестендіру нөмірі) енгізіңіз. ЖСН 12 саннан тұруы тиіс. \n\nДля поиска участка голосования введите Ваш ИИН (индивидуальный идентификационный номер). ИИН должен состоять из 12 цифр.")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    lang = 'Тілді таңдаңыз \nВыберите язык'
    db.insert_user(message.from_user.id, '')
    if not db.selectedCat(message.from_user.id)[3]:
        await bot.send_message(message.from_user.id, lang, parse_mode=types.ParseMode.HTML, reply_markup=nav.inline_kb1)

@dp.callback_query_handler()
async def process_callback_button1(callback_query: types.CallbackQuery):
    db.setLang(callback_query.from_user.id, callback_query.data)

    if db.getLang(callback_query.from_user.id) == "Қазақша":
        await bot.send_message(callback_query.from_user.id, "Аты-жөніңізді енгізіңіз")
    elif db.getLang(callback_query.from_user.id) == "Русский":
         await bot.send_message(callback_query.from_user.id, "Укажите Ваше ФИО")
    
@dp.message_handler()
async def response_message(msg: types.Message):

    if msg.text == "Қазақша" or db.getLang(msg.from_user.id) == "Қазақша":
        if msg.text == "Қазақша":
            db.setLang(msg.from_user.id, "Қазақша")
            await bot.send_message(msg.from_user.id, "Аты-жөніңізді енгізіңіз")
        
        else:

            if not db.userFioExists(msg.from_user.id):
                db.update_user(msg.from_user.id, msg.text)
                # await bot.send_message(msg.from_user.id, "Выберите категорию", reply_markup=nav.mainMenu)

            if msg.text == '1':
                db.updateCat(1, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)

            if msg.text == '2':
                db.updateCat(2, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)

            if msg.text == '3':
                db.updateCat(3, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)

            if msg.text == '4':
                db.updateCat(4, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)

            if msg.text == '5':
                db.updateCat(5, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)

            if msg.text == '6':
                db.updateCat(6, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)

            if msg.text == '7':
                db.updateCat(7, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)

            if msg.text == '8':
                db.updateCat(8, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)

            if msg.text == '9':
                db.updateCat(9, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)

            if msg.text == '10':
                db.updateCat(10, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)

            if msg.text == '11':
                db.updateCat(11, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)

            if msg.text == '12':
                db.updateCat(12, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Сұрағыңызды жазыңыз", parse_mode=types.ParseMode.HTML)
                    
            else:
                catSelected = db.selectedCat(msg.from_user.id)
                if catSelected[3] is None:
                    await bot.send_message(msg.from_user.id, "Сұрағыңыздың сипатын таңдаңыз", parse_mode=types.ParseMode.HTML)
                    await bot.send_message(msg.from_user.id, "1⃣ Тұрғын үй беру 🏠\n2⃣ Жұмыспен қамту жәнә әлеуметтік қамсыздандыру мәселелері 📄\n3⃣ Коммуналдық шаруашылық мәселелері 🚰\n4⃣ Білім беру мәселелері 👨🏻‍🎓\n5⃣ Денсаулық сақтау мәселелері 🏥\n6⃣ Кәсіпкерлік мәселелері 🏦\n7⃣ Ауылшаруашылығы мәселелері 🌽\n8⃣ Жер мәселесі 🌏\n9⃣ Қызмет бабын теріс пайдалану деректері 🙅🏻‍♂️\n1⃣0⃣ Заңдылық және құқықтық тәртіпті сақтау ⚖\n1⃣1⃣ Мәдениет саласы мәселелері 🎭\n1⃣2⃣ Басқа да мәселелер жөнінде ❔", parse_mode=types.ParseMode.HTML)
                else:
                    if not db.getLastQuest(msg.from_user.id):
                        if not msg.text.isnumeric():
                            db.setQuestion(msg.from_user.id, msg.text)
                            await bot.send_message(msg.from_user.id, "Рахмет, Сіздің сұрағыңыз қабылданды. Тағы сұрақ қою үшін /start батырмасын басыңыз", parse_mode=types.ParseMode.HTML)
                    else:
                        await bot.send_message(msg.from_user.id, "Тағы сұрақ қою үшін /start батырмасын басыңыз", parse_mode=types.ParseMode.HTML)
    
    elif msg.text == "Русский" or db.getLang(msg.from_user.id) == "Русский":
        if msg.text == "Русский":
            db.setLang(msg.from_user.id, "Русский")
            await bot.send_message(msg.from_user.id, "Ваш Фамилия Имя")
        
        else:

            if not db.userFioExists(msg.from_user.id):
                db.update_user(msg.from_user.id, msg.text)
                # await bot.send_message(msg.from_user.id, "Выберите категорию", reply_markup=nav.mainMenu)

            if msg.text == '1':
                db.updateCat(1, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)

            elif msg.text == '2':
                db.updateCat(2, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)

            elif msg.text == '3':
                db.updateCat(3, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)

            elif msg.text == '4':
                db.updateCat(4, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)

            elif msg.text == '5':
                db.updateCat(5, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)
                
            elif msg.text == '6':
                db.updateCat(6, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)

            elif msg.text == '7':
                db.updateCat(7, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)

            elif msg.text == '8':
                db.updateCat(8, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)

            elif msg.text == '9':
                db.updateCat(9, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)

            elif msg.text == '10':
                db.updateCat(10, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)

            elif msg.text == '11':
                db.updateCat(11, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)

            elif msg.text == '12':
                db.updateCat(12, msg.from_user.id)
                await bot.send_message(msg.from_user.id, "Напишите вопрос", parse_mode=types.ParseMode.HTML)


                                
                    
            else:
                catSelected = db.selectedCat(msg.from_user.id)
                if catSelected[3] is None:
                    await bot.send_message(msg.from_user.id, "Выберите характер Вашего вопроса", parse_mode=types.ParseMode.HTML)
                    await bot.send_message(msg.from_user.id, "1⃣ Вопросы обеспечения жильём 🏠\n2⃣ Вопросы трудоустройства и социального обеспечения 📄\n3⃣ Вопросы коммунального хозяйства 🚰\n4⃣ Вопросы образования 👨🏻‍🎓\n5⃣ Вопросы здравоохранения 🏥\n6⃣ Вопросы предпринимательства 🏦\n7⃣ Вопросы сельского хозяйства 🌽\n8⃣ Земельные вопросы 🌏\n9⃣ Факты ненадлежащего использования служебного положения 🙅🏻‍♂️\n1⃣0⃣ Соблюдение законодательной и правовой дисциплины ⚖\n1⃣1⃣ Вопросы сферы культуры 🎭\n1⃣2⃣ Другие вопросы ❔", parse_mode=types.ParseMode.HTML)

                else:
                    if not db.getLastQuest(msg.from_user.id):
                        if not msg.text.isnumeric():
                            db.setQuestion(msg.from_user.id, msg.text)
                        await bot.send_message(msg.from_user.id, "Спасибо, Ваш вопрос принят. Чтобы отправить еще вопросы нажмите /start", parse_mode=types.ParseMode.HTML)
                    else:
                        await bot.send_message(msg.from_user.id, "Чтобы отправить еще вопросы нажмите /start", parse_mode=types.ParseMode.HTML)



    
    # else:
    #     await bot.send_message(msg.from_user.id, "Вы уже выбрали категорию вопрос", parse_mode=types.ParseMode.HTML)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
