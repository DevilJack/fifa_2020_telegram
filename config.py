from aiohttp import BasicAuth
from aiogram import types
from keyboards import ListOfButtons
from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")

TOKEN = config['token'][TOKEN]

BOT_URL = config['bot_url']['BOT_URL']

ADMINS_IDS = (config['chat_ids']['BOSS_ID'], config['chat_ids']['KUSHER_ID'])

#|-------------------- PROXIE ----------------| # прокси Кирилла
PROXIE_URL = config['proxie']['PROXIE_URL']

PROXIE_LOGIN = config['proxie']['PROXIE_LOGIN']

PROXIE_PASSWORD = config['proxie']['PROXIE_PASSWORD']

PROXIE_AUTH = BasicAuth(
    login = PROXIE_LOGIN,
    password = PROXIE_PASSWORD
)

PROXIE_URL_W_AUTH = config['proxie']['PROXIE_URL_W_AUTH']

MAIN_KEYBOARD = ListOfButtons(
    text = [
        'Играть', 
        'Активные турниры',
        'Архив турниров',
        'Добавить команду',
        'Добавить игрока',
        'Сформировать турнир',
        'Добавить турнир'
    ],
    align = [1, 2, 2, 2]
).reply_keyboard

MAIN_KEYBOARD_2 = ListOfButtons(
    text = [
        'Играть', 
        'Команды',
        'Игроки',
        'Турниры'
    ],
    align = [1, 2, 1]
).reply_keyboard

TOURNS_MENU = ListOfButtons(
    text = [
        'Активные турниры', 
        'Архив турниров',
        'Добавить турнир',
        'Сформировать турнир',
        'Назад на главную'
    ],
    align = [2, 2, 1]
).reply_keyboard

TEAMS_MENU = ListOfButtons(
    text = [
        'Добавить команду',
        'Назад на главную'
    ],
    align = [1, 1]
).reply_keyboard

PLAYERS_MENU = ListOfButtons(
    text = [
        'Добавить игрока',
        'Подтвердить участие',
        'Назад на главную'
    ],
    align = [1, 1, 1]
).reply_keyboard

START_PLAYING_KEYBOARD = ListOfButtons(
    text = [
        'Начать',
        'Отмена'
    ],
    align = [1, 1]
).reply_keyboard

HIT_KEYBOARD = ListOfButtons(
    text = [
        'Удар в левый угол',
        'Удар по центру',
        'Удар в правый угол'
    ],
    callback=["hit_left", "hit_center", "hit_right"],
    align = [1, 1, 1]
).inline_keyboard

BLOCK_KEYBOARD = ListOfButtons(
    text = [
        'Защитить левый угол и центр',
        'Защитить правый угол и центр',
        'Угадать угол'
    ],
    callback=["block_left_center", "block_right_center", "block_left_right"],
    align = [1, 1, 1]
).inline_keyboard

SUPPORT_KEYBOARD = ListOfButtons(
    text = [
        'Поддержать!🎉'
    ],
    align = [1]
).reply_keyboard

#⚽️🚫🥅🔥🎬⌚️

GOAL_RESULT = {
    (0, 0): ("СЕЙВ!", "отбивает мяч, летящий в левый угол!🥅", "в блестящем прыжке парирует удар в левый нижний угол!🥅", "делает сумасшедший сейв и тащит мяч из левой девятки!🥅", "ногой выбивает мяч, летевший в левый нижний угол!🥅", "кончиками пальцев переводит в крестовину мяч, летевший в левый верхний угол!🥅", False),
    (0, 1): ("ГОЛ!", "забивает мяч в левый угол!🔥", "красивейшим ударом забивает мяч в левую девятку!🔥", "забивает мяч ювелирным ударом от штанги в левый нижний угол!🔥", "хитрым крученым ударом кладет мяч в левую девятку!🔥", "обманывает вратаря, и мяч медленно закатывается в левый нижний угол. Обидно.", True),
    (0, 2): ("СЕЙВ!", "Мяч попал в левую штангу!🥅", "Мяч попал в левую штангу!🥅", "Мяч попал в левую штангу!🥅", "Мяч попал в левую штангу!🥅", "Мяч попал в левую штангу!🥅", False),
    (1, 0): ("СЕЙВ!", "отбивает мяч, летящий в центр!🥅", "отбивает мощнейший удар по центру ворот!🥅", "не поддался на хитрости и намертво взял удар по центру!🥅", "кулаками отбивает мяч, летевший под самую перекладину!🥅", "ногами выбивает мяч, летевший как пуля по центру ворот!🥅", False),
    (1, 1): ("СЕЙВ!", "отбивает мяч, летящий в центр!🥅", "отбивает мощнейший удар по центру ворот!🥅", "не поддался на хитрости и намертво взял удар по центру!🥅", "кулаками отбивает мяч, летевший под самую перекладину!🥅", "ногами выбивает мяч, летевший как пуля по центру ворот!🥅", False),
    (1, 2): ("ГОЛ!", "забивает мяч в центр!🔥", "словно Роберто Карлос мощнейшим ударом забивает гол ударом по центру ворот!🔥", "обманывает вратаря и забивает ему между ног!🔥", "коварным ударом с отскоком от земли забивает ударом по центру ворот!🔥", "парашютиком перекидывает упавшего вратаря и забивает ударом по центру ворот!🔥", True),
    (2, 0): ("ГОЛ!", "забивает мяч в правый угол!🔥", "красивейшим ударом забивает мяч в правую девятку!🔥", "забивает мяч ювелирным ударом от штанги в правый нижний угол!🔥", "хитрым крученым ударом кладет мяч в левую девятку!🔥", "обманывает вратаря, и мяч медленно закатывается в правый нижний угол. Обидно.", True),
    (2, 1): ("СЕЙВ!", "отбивает мяч, летящий в правый угол!🥅", "в блестящем прыжке парирует удар в правый нижний угол!🥅", "делает сумасшедший сейв и тащит мяч из правой девятки!🥅", "ногой выбивает мяч, летевший в правый нижний угол!🥅", "кончиками пальцев переводит в крестовину мяч, летевший в правый верхний угол!🥅", False),
    (2, 2): ("СЕЙВ!", "Мяч попал в правую штангу!🥅", "Мяч попал в правую штангу!🥅", "Мяч попал в правую штангу!🥅", "Мяч попал в правую штангу!🥅", "Мяч попал в правую штангу!🥅", False)
}

SHORT_GOAL_RESULT = {
    (0, 0): "СЕЙВ!",
    (0, 1): "ГОЛ!",
    (0, 2): "СЕЙВ!",
    (1, 0): "СЕЙВ!",
    (1, 1): "СЕЙВ!",
    (1, 2): "ГОЛ!",
    (2, 0): "ГОЛ!",
    (2, 1): "СЕЙВ!",
    (2, 2): "СЕЙВ!"
}

HIT_RESULT = {
    'hit_left': 0,
    'hit_center': 1,
    'hit_right': 2
}

BLOCK_RESULT = {
    'block_left_center': 0,
    'block_right_center': 1,
    'block_left_right': 2
}

PLAY_ROUND_KEYBOARD = ListOfButtons(
    text = [
        'Начать',
        'Отмена'
    ],
    callback=["start_round", "cancel_round"],
    align = [1, 1]
).inline_keyboard

MAIN_CANCEL = ListOfButtons(
    text = [
        'Отменить действие'
    ],
    callback=["main_cancel"],
    align = [1]
).inline_keyboard
