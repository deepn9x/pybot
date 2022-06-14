from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# --- Cats ---

btnC1 = KeyboardButton('Вопросы обеспечения жильём')
btnC2 = KeyboardButton('Вопросы трудоустройства и социального обеспечения')
btnC3 = KeyboardButton('Вопросы коммунального хозяйства')
btnC4 = KeyboardButton('Вопросы образования')
btnC5 = KeyboardButton('Вопросы здравоохранения')
btnC6 = KeyboardButton('О вопросах предпринимательства')
btnC7 = KeyboardButton('Вопросы сельского хозяйства')
btnC8 = KeyboardButton('Земельные вопросы')
btnC9 = KeyboardButton('Факты ненадлежащего использования служебного положения')
btnC10 = KeyboardButton('Соблюдение законодательной и правовой дисциплины')
btnC11 = KeyboardButton('Вопросы сферы культуры')
btnC12 = KeyboardButton('О других вопросах')

btnC1kk = KeyboardButton('Тұрғын үй беру')
btnC2kk = KeyboardButton('Жұмыспен қамту жәнә әлеуметтік қамсыздандыру мәселелері')
btnC3kk = KeyboardButton('Коммуналдық шаруашылық мәселелері')
btnC4kk = KeyboardButton('Білім беру мәселелері')
btnC5kk = KeyboardButton('Мәдениет саласы мәселелері')
btnC6kk = KeyboardButton('Кәсіпкерлік мәселелері жөнінде')
btnC7kk = KeyboardButton('Ауылшаруашылығы мәселелері')
btnC8kk = KeyboardButton('Жер мәселесі')
btnC9kk = KeyboardButton('Қызмет бабын теріс пайдалану деректері')
btnC10kk = KeyboardButton('Заңдылық және құқықтық тәртіпті сақтау')
btnC11kk = KeyboardButton('Мәдениет саласы мәселелері')
btnC12kk = KeyboardButton('Басқа да мәселелер жөнінде')

btnKaz = KeyboardButton("Қазақша")
btnRu = KeyboardButton("Русский")

btnCatSelected = KeyboardButton("Категория выбрана")
btnCatSelectedKk = KeyboardButton("Сұрақ сипаты таңдалды")



#, btnC2, btnC3, btnC4, btnC5, btnC6, btnC7, btnC8, btnC9, btnC10, btnC11

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnC1).row(btnC2).row(btnC3).row(btnC4).row(btnC5).row(btnC6).row(btnC7).row(btnC8).row(btnC9).row(btnC10).row(btnC11).row(btnC12)
mainMenuKk = ReplyKeyboardMarkup(resize_keyboard=True).row(btnC1kk).row(btnC2kk).row(btnC3kk).row(btnC4kk).row(btnC5kk).row(btnC6kk).row(btnC7kk).row(btnC8kk).row(btnC9kk).row(btnC10kk).row(btnC11kk)


langMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnKaz).row(btnRu)


catSelected = ReplyKeyboardMarkup(resize_keyboard=True).row(btnCatSelected)
catSelectedKk = ReplyKeyboardMarkup(resize_keyboard=True).row(btnCatSelectedKk)



inline_btn_1 = InlineKeyboardButton('🇰🇿 Қазақша', callback_data='Қазақша')
inline_btn_2 = InlineKeyboardButton('🇷🇺 Русский', callback_data='Русский')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)


# inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
# inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='btn2'))
# inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
# inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
# inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
# inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
# inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
# inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
# inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
# inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
# inline_kb_full.add(InlineKeyboardButton('Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/'))
