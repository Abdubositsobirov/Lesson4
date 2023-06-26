from aiogram.types import Message
from main import *
from states import *
from config import *
from keyboard import *

@dp.message_handler(commands=['start'])
async def cmd_welcome(message: Message):
    username = message.from_user.username
    user_fullname = message.from_user.full_name
    await message.reply(f"Welcome{username}")
    await message.answer(f"Welcome{username}")

@dp.message_handler(commands=['help'])
async def cmd_help(message:Message):
    text = f"This bot help increase your programing skills"
    await message.answer(text)

@dp.message_handler(commands=['callofdutyinfo'])
async def cmd_callofdutyinfo(message:Message):
    text = f"How Many Call of Duty Games Are There? There are forty-two games in the entire Call of Duty franchise. Sixteen of them are included in the main series, including the Modern Warfare and Black Ops storylines"
    await message.answer(text)

@dp.message_handler(commands=['callofdutymalumot'])
async def cmd_callofdutymalumot(message:Message):
    text = f"Qancha Call of Duty o'yinlari mavjud? Butun Call of Duty franshizasida qirq ikkita o'yin mavjud. Ulardan o'n oltitasi asosiy seriyaga kiritilgan, jumladan, Zamonaviy urush va Black Ops hikoyalari"
    await message.answer(text)

@dp.message_handler(commands=['MW3info'])
async def cmd_MW3info(message:Message):
    text = f"Call of Duty: Modern Warfare 3 (сокращается до Modern Warfare 3, COD: MW3 и MW3) — мультиплатформенная компьютерная игра в жанре шутер от первого лица, сиквел Call of Duty: Modern Warfare 2, восьмая игра в серии Call of Duty. Разработана компанией Infinity Ward совместно со студиями Sledgehammer Games и Raven Software, издателем игры выступила Activision. Разработкой версии игры для консоли Nintendo DS занималась студия n-Space[5], версии для Wii — Treyarch[6], версия для Mac — Aspyr Media (вышла во второй половине мая 2014 года)[7]. Игра поступила в продажу 8 ноября 2011 года на всех платформах[8]. Третий год подряд игра серии Call of Duty установила мировой рекорд продаж в игровой сфере: за 24 часа было продано более 6,5 млн копий игры[9]"
    await message.answer(text)

@dp.message_handler(commands=['MW3malumot'])
async def cmd_MW3malumot(message:Message):
    text = f"Call of Duty: Modern Warfare 3 (qisqartirilgan Modern Warfare 3, COD: MW3 va MW3) — Call of Duty: Modern Warfare 2 ning ko‘p platformali birinchi shaxs otishma video o‘yinining davomi, Call of Duty seriyasidagi sakkizinchi o‘yin. . Infinity Ward tomonidan Sledgehammer Games va Raven Software bilan hamkorlikda ishlab chiqilgan o'yin Activision tomonidan nashr etilgan. Nintendo DS versiyasi n-Space[5] tomonidan, Wii versiyasi Treyarch[6] va Mac versiyasi Aspyr Media tomonidan ishlab chiqilgan (2014 yil may oyining ikkinchi yarmida chiqarilgan)[7]. O'yin 2011 yil 8 noyabrda barcha platformalarda sotuvga chiqdi[8]. Ketma-ket uchinchi yil Call of Duty o'yini 24 soat ichida 6,5 ​​million nusxada sotilgan bilan jahon o'yin rekordini o'rnatdi"
    await message.answer(text)

@dp.message_handler(commands=['Menu'])
async def cmd_Menu(message:Message):
    text = f"/help=Yordam:/callofdutymalumot = O'yin haqida malumot UZB:/callofdutyinfo=O'yin haqida malumot ENG:/MW3info=MW3 o'yini haqida malumot RUS:/MW3malumot=MW3 o'yini haqida malumot"
    await message.answer(text)