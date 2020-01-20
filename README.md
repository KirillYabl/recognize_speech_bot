# Speech recognition bots (VK and telegram with dialogflow integration)

[](demo_tg_bot.gif)
[](demo_vk_bot.gif)

This project contain code for create your bots in VK and Telegram.

Both, VK in Telegram bots are integrated with dialogflow by google.

Project also contain code which helps you training dialogflow agent.

### How to install

##### Local

You need to create `.env` file and write in file parameters:

1. `TG_BOT_TOKEN` - secret token for your telegram bot. Just use [this](https://core.telegram.org/bots#creating-a-new-bot) instruction (use VPN to open this link in Russia).
    1. After you got `TG_BOT_TOKEN` you need to write to you bot in telegram any message (`/start` for example).
2. `DF_PROJECT_ID` - your project id in dialogflow. [instruection](https://cloud.google.com/dialogflow/docs/quick/setup)
3. `DF_CREDENTIALS_PATH` - path to your secret dialogflow file. [create agent](https://cloud.google.com/dialogflow/docs/quick/build-agent), [create file](https://cloud.google.com/docs/authentication/getting-started)
4. `DF_SESSION_ID` - session id in dialogflow, you can choose random number like 123456789
5. `DF_LANGUAGE_CODE` - language of your agent. Add language to agent in settings.
6. `VK_APP_TOKEN` - secret token of you VK app. You can create this in group administration panel in `Work with API`.
7. `PROXY` - proxy IP with port and https if you need. Work with empty proxy if you in Europe.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

##### Deploy on heroku

For deploy this bot on [heroku](https://heroku.com) you need to do next:

1) Sign up in heroku
2) Create app
3) Clone this repository and download on heroku with GitHub method (tab `Deploy` in heroku app)
4) Add `Config Vars` in `Settings` tab in heroku app like in `Local` but,
    1) `DF_CREDENTIALS_PATH`=`google-credentials.json`
    2) Add in `Config Vars` `GOOGLE_CREDENTIALS` which equal content in your secret dialogflow file.
    
### How to use

##### Run in Local

Open command line (in windows `Win+R` and write `cmd` and `Ok`). Go to directory with program or just write in cmd:

Create your own `training_intents.json` file with training questions and answers for dialogflow.

Example of training file:

{
    "Устройство на работу": {
        "questions": [
            "Как устроиться к вам на работу?",
            "Как устроиться к вам?",
            "Как работать у вас?",
            "Хочу работать у вас",
            "Возможно-ли устроиться к вам?",
            "Можно-ли мне поработать у вас?",
            "Хочу работать редактором у вас"
        ],
        "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
    },
    "Забыл пароль": {
        "questions": [
            "Не помню пароль",
            "Не могу войти",
            "Проблемы со входом",
            "Забыл пароль",
            "Забыл логин",
            "Восстановить пароль",
            "Как восстановить пароль",
            "Неправильный логин или пароль",
            "Ошибка входа",
            "Не могу войти в аккаунт"
        ],
        "answer": "Если вы не можете войти на сайт, воспользуйтесь кнопкой «Забыли пароль?» под формой входа. Вам на почту прийдёт письмо с дальнейшими инструкциями. Проверьте папку «Спам», иногда письма попадают в неё."
    }
}

```

{
    INTENT_THEME: {
        "questions": INTENT_QUESTIONS,
        "answer": INTENT_ANSWER
    },
    INTENT_THEME: {
        "questions": INTENT_QUESTIONS,
        "answer": INTENT_ANSWER
    }
}

:param INTENT_THEME: str, name of your intent in dialogflow
:param INTENT_QUESTIONS: list of str, list of questions for training
:param INTENT_ANSWER: str, answer for questions

```

`python <PATH TO PROGRAM>\training_dialogflow.py` training your agent

`python <PATH TO PROGRAM>\telegram_bot.py` if you want to start telegram bot.

`python <PATH TO PROGRAM>\vk_bot.py` if you want to start vk bot.

##### Deploy on heroku

Run bot in `Resources` tab in heroku app. `Procfile` for run in repo already.

### References

[telegram bots documentation](https://core.telegram.org/bots#creating-a-new-bot)

[heroku](https://heroku.com)

[VK API documentation](https://vk.com/dev/first_guide)

[dialogflow documentation](https://cloud.google.com/dialogflow/docs/)

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
