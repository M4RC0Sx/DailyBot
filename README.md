# DailyBot
Simple DailyBot made using Python Telegram API. It just schedules your timetable based on a JSON file and sends you alerts via telegram 10 minutes before a class is going to start or finish, telling you the place where it is going to take place.

## Requeriments
* Python3
* Python3 - logging
* Python3 - json
* Python3 - os
* Python3 - schedule
* Python3 - time

## Instructions
1. Clone the repository.
2. Edit the file DailyBot.py and change the constants **BOT_TOKEN** and **CHAT_ID** according to your Telegram Bot. (You must create it and get this params via BotFather).
3. Edit the file timetable.json according to your daily routine. **It is very important that you follow the same format in the hours.**
4. Run the bot on your server, raspberry... A good idea is to create a screen for it and attach it there.
5. **IMPORTANT: You must execute the command /timetable everytime you init the bot in order to load de JSON data from the file.**

## Additional Notes
*I made this bot to learn abount Python Telegram API and to my daily usage. It has some hard-coded aspects and some ugly things inside it. Maybe I could do a better version and recode it. Sorry for that :P*

## Some Screenshots
<img src="https://i.imgur.com/3lIW0tg.png" title="Screenshot#1 - General Screenshot">