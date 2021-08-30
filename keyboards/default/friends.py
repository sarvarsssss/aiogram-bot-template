from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menufriends = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Izzat"),
            KeyboardButton(text="Jamshid"),
            KeyboardButton(text="Xabibullo"),

        ],
        [
            KeyboardButton(text="Ibrohim"),
            KeyboardButton(text="Islom"),
            KeyboardButton(text="Jamol"),
        ],
        [
            KeyboardButton(text="Shohjahon"),
            KeyboardButton(text="Ilyos"),
        ],
        [
            KeyboardButton(text="Log Out"),
        ],
    ],
    resize_keyboard=True
)
