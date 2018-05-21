import telepot
import time
from telepot.namedtuple import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton


bot = telepot.Bot('456608249:AAGAKmsi_iaPsPtJ7tvRAMUQw0AS5xvb4vE')

def menu():
        askaim = ReplyKeyboardMarkup(keyboard =
                [
                [KeyboardButton(text = 'News Feeds')],
                [KeyboardButton(text = 'Project Examples')],
                [KeyboardButton(text = 'Back to main menu.')],
                ],
                )
        return askaim

def form():
        askform = ReplyKeyboardMarkup(keyboard =
                [
                [KeyboardButton(text = 'Title&Date&Full Text')],
                [KeyboardButton(text = 'Title&Date&URL')],
                ],
                )
        return askform

def newstypeFT():
        news_type = InlineKeyboardMarkup(inline_keyboard =
                [
                [InlineKeyboardButton(text = 'Software News', callback_data='Software News FT')],
                [InlineKeyboardButton(text = 'Electronics News', callback_data='Electronics News FT')],
                [InlineKeyboardButton(text = 'Hardware News', callback_data='Hardware News FT')],
                ]
                )
        return news_type

def newstypeURL():
        news_type = InlineKeyboardMarkup(inline_keyboard =
                [
                [InlineKeyboardButton(text = 'Software News', callback_data='Software News URL')],
                [InlineKeyboardButton(text = 'Electronics News', callback_data='Electronics News URL')],
                [InlineKeyboardButton(text = 'Hardware News', callback_data='Hardware News URL')],                 
                ]
                )
        return news_type

def projectype():
        project_type = ReplyKeyboardMarkup(keyboard =
                [
                [KeyboardButton(text = 'Arduino')],
                [KeyboardButton(text = 'RaspberryPi')],
                [KeyboardButton(text = 'Back to type choosing')],
                ],
                )
        return project_type

def nextfiveras():
        nextfive = ReplyKeyboardMarkup(keyboard =
                [
                [KeyboardButton(text = 'Please load five more RaspberryPi examples for me.')],
                [KeyboardButton(text = 'Return to project-type-choosing menu.')],
                ],
                )
        return nextfive

def nextfiveard():
        nextfive = ReplyKeyboardMarkup(keyboard =
                [
                [KeyboardButton(text = 'Please load five more Arduino examples for me.')],
                [KeyboardButton(text = 'Return to project-type-choosing menu.')],
                ],
                )
        return nextfive



        

