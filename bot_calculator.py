# Задача 2. Прикрутить бота к задачам с предыдущего семинара:
# 1. Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from math import *
import logger as lg

result = 0
text = ''


def create():
    global result
    global text
    data = result
    my_text = text
    lg.calc_logger(my_text, data)
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '<p {}>math expression: {} = {} </p>\n'\
        .format(style, my_text, data)
    with open('index.html', 'w') as page:
        page.write(html)

    return html


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global result
    global text
    text = update.message.text
    if 'j' not in text:                                     # Калькулятор целых чисел
        text_1 = text.split()
        if len(text_1) != 3:
            return
        a = int(text_1[0])
        b = int(text_1[2])
        operator = text_1[1]
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b
        elif operator == '^':
            result = pow(a, b)
        await update.message.reply_text(f'Ответ: {result}')
    elif 'j' in text:                                       # Калькулятор комплексных чисел
        text.replace("(", "")
        text.replace(")", "")
        text_1 = text.split()
        if len(text_1) != 3:
            return
        a = complex(text_1[0])
        b = complex(text_1[2])
        operator = text_1[1]
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b
        await update.message.reply_text(f'Ответ: {result}')
    print(create())


app = ApplicationBuilder().token(
    "5408193276:AAH29vRgDIHfCbTSj5bJJw0Bq_zwdjRFNzU").build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calc))
app.add_handler(CommandHandler("hello", hello))


app.run_polling()
