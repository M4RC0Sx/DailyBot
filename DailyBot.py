import logging
import json
import os
import schedule
import time
from datetime import datetime, timedelta

from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram import ParseMode


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s\
                            - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

CHAT_ID = "INSERT_YOUR_CHAT_ID_HERE"
BOT_TOKEN = "INSERT_YOUR_BOT_TOKEN_HERE"


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def timetable(update, context):

    print(CHAT_ID)
    print(context.bot)

    load_schedule(context)

    timetable_path = os.path.dirname(
        os.path.realpath('__file__')) + '/timetable.json'

    result = ''

    with open(timetable_path, 'r') as f:
        timetable_data = json.loads(f.read())
        f.close()

    for item in timetable_data['Week']:
        for day in item:
            result += ('<b>[' + day + ']</b>\n')
            for subject in item[day]:
                result += '<i>' + \
                    subject['Subject'] + '</i> - (' + subject['Start'] + \
                    '-' + subject['End'] + ') - ' + subject['Place'] + '\n'
            result += '\n'
    result += ''

    context.bot.send_message(chat_id=CHAT_ID,
                             text=result,
                             parse_mode=ParseMode.HTML)


def load_schedule(context):

    timetable_path = os.path.dirname(
        os.path.realpath('__file__')) + '/timetable.json'
    schedule.clear()

    with open(timetable_path, 'r') as f:
        timetable_data = json.loads(f.read())
        f.close()

    for item in timetable_data['Week']:
        for day in item:
            s_day = str(day)
            for subject in item[day]:
                s_subject = subject['Subject']

                start_time = datetime.strptime(
                    subject['Start'], "%H:%M") - timedelta(minutes=10)
                end_time = datetime.strptime(
                    subject['End'], "%H:%M") - timedelta(minutes=10)

                s_start = start_time.strftime("%H:%M")
                s_end = end_time.strftime("%H:%M")

                s_place = subject['Place']

                if s_day == 'Monday':
                    schedule.every().monday.at(s_start).do(send_start_message,
                                                           context=context, subject=s_subject, place=s_place)
                    schedule.every().monday.at(s_end).do(
                        send_end_message, context=context, subject=s_subject)
                elif s_day == 'Tuesday':
                    schedule.every().tuesday.at(s_start).do(send_start_message,
                                                            context=context, subject=s_subject, place=s_place)
                    schedule.every().tuesday.at(s_end).do(
                        send_end_message, context=context, subject=s_subject)
                elif s_day == 'Wednesday':
                    schedule.every().wednesday.at(s_start).do(send_start_message,
                                                              context=context, subject=s_subject, place=s_place)
                    schedule.every().wednesday.at(s_end).do(
                        send_end_message, context=context, subject=s_subject)
                elif s_day == 'Thursday':
                    schedule.every().thursday.at(s_start).do(send_start_message,
                                                             context=context, subject=s_subject, place=s_place)
                    schedule.every().thursday.at(s_end).do(
                        send_end_message, context=context, subject=s_subject)
                elif s_day == 'Friday':
                    schedule.every().friday.at(s_start).do(send_start_message,
                                                           context=context, subject=s_subject, place=s_place)
                    schedule.every().friday.at(s_end).do(
                        send_end_message, context=context, subject=s_subject)
                elif s_day == 'Saturday':
                    schedule.every().saturday.at(s_start).do(send_start_message,
                                                             context=context, subject=s_subject, place=s_place)
                    schedule.every().saturday.at(s_end).do(
                        send_end_message, context=context, subject=s_subject)
                elif s_day == 'Sunday':
                    schedule.every().sunday.at(s_start).do(send_start_message,
                                                           context=context, subject=s_subject, place=s_place)
                    schedule.every().sunday.at(s_end).do(
                        send_end_message, context=context, subject=s_subject)
                print(s_start)
                print(s_end)


def send_start_message(context, subject, place):
    result = '<b>INFO:</b> ' + '<i>' + subject + '</i>' + \
        ' is starting at ' + place + ' in 10 minutes!\n'

    context.bot.send_message(chat_id=CHAT_ID,
                             text=result,
                             parse_mode=ParseMode.HTML)


def send_end_message(context, subject):
    result = '<b>INFO:</b> ' + '<i>' + subject + \
        '</i>' + ' is ending in 10 minutes!\n'

    context.bot.send_message(chat_id=CHAT_ID,
                             text=result,
                             parse_mode=ParseMode.HTML)


def test(update, context):
    print(update.effective_chat.id)


def main():
    
    updater = Updater(token=BOT_TOKEN,
                      use_context=True)
    dispatcher = updater.dispatcher

    timetable_handler = CommandHandler('timetable', timetable)
    dispatcher.add_handler(timetable_handler)

    test_handler = CommandHandler('test', test)
    dispatcher.add_handler(test_handler)

    updater.start_polling()
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    load_schedule(None)
