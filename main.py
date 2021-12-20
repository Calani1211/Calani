import markup as markup
import telebot
from telebot import types

# Название телеграм бота HelpForStudents_RGSU_bot
TOKEN = '5026323173:AAHfiGMC21MAWt_ysuzdbCaX9DuqyzGCS_Q'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_text(message):
        bot.send_message(message.chat.id, ' Добро пожаловать в HelpForStudents_RGSU_bot! Все управление ботом осуществляется с помощью кнопок✨- Вы можете посмотреть актуальное расписание преподавателя своей или другой группы ✌️- Актуальное расписание каждые 7 утра ✨- Напоминание о начале пары 🔥- Если что-то произойдет и вы застрянете где-то, то вам в помощь /start Для дальнейших действий введите команду /info' )

@bot.message_handler(commands=['info'])
def text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('ИН-КОД-2020-2-11')
    item2 = types.KeyboardButton('ИН-КОД-2019-1')
    item3 = types.KeyboardButton('БД-К-0-Д-2020-1')
    item4 = types.KeyboardButton('БД-К-0-Д-2021-2-11')
    item5 = types.KeyboardButton('ПО-К-0-Д-2021-1')
    item6 = types.KeyboardButton('РП-К-0-Д-2020-2-11')

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, 'Выберите группу',format(message.from_user), reply_markup = markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'ИН-КОД-2020-2-11':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Расписание 20-2-11')
            item2 = types.KeyboardButton('Группа ИН-КОД-2020-2-11')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Что вас интересует?', format(message.from_user), reply_markup=markup)

        if message.chat.type == 'private':
            if message.text == 'Расписание ИН-КОД-2020-2-11':
                bot.send_photo(message.chat.id, 'https://ibb.co/chPptZm')

        if message.chat.type == 'private':
            if message.text == 'Группа ИН-КОД-2020-2-11':
                bot.send_message(message.chat.id,
                                 ' 1. Бойцан Александр;                                                                                                       2. Вертегел Роман;                                                                                                                                             3. Волков Максим;                                                                                                                                   4. Вулканов Антон;                                                                                                                                             5. Козелев Сергей;                                                                                                                                                                                6. Копцева Яна;                                                                                                                                                                                                                   7. Кузьмин Павел;                                                                                                                                                                                8. Московкин Николай;                                                                                                                                                                                9. Нещадова Валерия;                                                                                                                                                                                10. Семёнов Алексей;                                                                                                                                                                                                                   11. Собиров Данил;                                                                                                                                                                                12. Хитрова Анастасия;                                                                                                                                                                                                                   13. Ховалыг Артыш;                                                                                                                                                                                                                   14. Чабров Владислав;                                                                                                                                                                                                                   15. Чайковский Никита;                                                                                                                                                                                                                                                      16.  Чикинда Анатолий;')


        if message.text == 'ИН-КОД-2019-1':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Расписание ИН-КОД-2019-1')
            item2 = types.KeyboardButton('Группа ИН-КОД-2019-1')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Что вас интересует?', format(message.from_user), reply_markup=markup)

        if message.chat.type == 'private':
            if message.text == 'Расписание 19-1':
                bot.send_photo(message.chat.id, 'https://ibb.co/wrVRs9Q')
                bot.send_photo(message.chat.id, 'https://ibb.co/DCggCX3')

        if message.chat.type == 'private':
            if message.text == 'Группа ИН-КОД-2019-1':
                bot.send_message(message.chat.id,
                                 '1. Воробьёва Анастасия;                                                                                                       2. Давлетов Алимурат;                                                                                                       3. Иванов Даниил;                                                                                                       4. Колпакова Екатерина;                                                                                                       5. Корысткина Александра;                                                                                                       6. Ларцева Василиса;                                                                                                       7. Лебедев Артём;                                                                                                       8. Махмудов Самир;                                                                                                       9. Мельников Дмитрий;                                                                                                       10. Митусов Данила;                                                                                                       11. Никулин Дмитрий;                                                                                                       12. Рюмшина Регина;                                                                                                       13. Савунова Татьяна;                                                                                                       14. Семёнов Алексей;                                                                                                       15. Тимиряев Илья;                                                                                                       16. Урванцева Анастасия;                                                                                                       17. Хамдан Радуан;                                                                                                       18. Чериков Алексей;')


            if message.text == 'БД-К-0-Д-2020-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Расписание БД-К-0-Д-2020-1')
                item2 = types.KeyboardButton('Группа БД-К-0-Д-2020-1')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, back)

                bot.send_message(message.chat.id, 'Что вас интересует?', format(message.from_user), reply_markup=markup)


            if message.chat.type == 'private':
                if message.text == 'Расписание БД-К-0-Д-2020-1':
                    bot.send_photo(message.chat.id, 'https://imgur.com/BA0tjTV')
                    bot.send_photo(message.chat.id, 'https://imgur.com/CHZWO53')

            if message.chat.type == 'private':
                if message.text == 'Группа БД-К-0-Д-2020-1':
                    bot.send_message(message.chat.id,'')



            if message.text == 'БД-К-0-Д-2021-2-11':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Расписание БД-К-0-Д-2021-2-11')
                item2 = types.KeyboardButton('Группа БД-К-0-Д-2021-2-11')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, back)

                bot.send_message(message.chat.id, 'Что вас интересует?', format(message.from_user), reply_markup=markup)

            if message.chat.type == 'private':
                if message.text == 'Расписание БД-К-0-Д-2021-2-11':
                    bot.send_photo(message.chat.id, 'https://imgur.com/undefined')
                    bot.send_photo(message.chat.id, 'https://imgur.com/undefined')

            if message.chat.type == 'private':
                if message.text == 'Группа БД-К-0-Д-2021-2-11':
                    bot.send_message(message.chat.id,'')



            if message.text == 'ПО-К-0-Д-2021-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Расписание ПО-К-0-Д-2021-1')
                item2 = types.KeyboardButton('Группа ПО-К-0-Д-2021-1')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, back)

                bot.send_message(message.chat.id, 'Что вас интересует?', format(message.from_user), reply_markup=markup)

            if message.chat.type == 'private':
                if message.text == 'Расписание ПО-К-0-Д-2021-1':
                    bot.send_photo(message.chat.id, 'https://imgur.com/undefined')
                    bot.send_photo(message.chat.id, 'https://imgur.com/undefined')

            if message.chat.type == 'private':
                if message.text == 'Группа ПО-К-0-Д-2021-1':
                    bot.send_message(message.chat.id,'')



            if message.text == 'РП-К-0-Д-2020-2-11':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Расписание РП-К-0-Д-2020-2-11')
                item2 = types.KeyboardButton('Группа РП-К-0-Д-2020-2-11')
                back = types.KeyboardButton('Назад')
                markup.add(item1, item2, back)

                bot.send_message(message.chat.id, 'Что вас интересует?', format(message.from_user), reply_markup=markup)

            if message.chat.type == 'private':
                if message.text == 'Расписание РП-К-0-Д-2020-2-11':
                    bot.send_photo(message.chat.id, 'https://imgur.com/undefined')
                    bot.send_photo(message.chat.id, 'https://imgur.com/undefined')

            if message.chat.type == 'private':
                if message.text == 'Группа РП-К-0-Д-2020-2-11':
                    bot.send_message(message.chat.id,'')

        if message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            item1 = types.KeyboardButton('ИН-КОД-2020-2-11')
            item2 = types.KeyboardButton('ИН-КОД-2019-1')
            item3 = types.KeyboardButton('БД-К-0-Д-2020-1')
            item4 = types.KeyboardButton('БД-К-0-Д-2021-2-11')
            item5 = types.KeyboardButton('ПО-К-0-Д-2021-1')
            item6 = types.KeyboardButton('РП-К-0-Д-2020-2-11')

            markup.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(message.chat.id, 'Выберите группу', format(message.from_user), reply_markup=markup)



bot.polling(none_stop=True)