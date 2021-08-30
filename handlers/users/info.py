from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, photo_size
from keyboards.default.friends import menufriends
from loader import dp

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id(message: types.Message):
    await message.reply(message.photo[-1].file_id)



@dp.message_handler(CommandStart())
async def show_menu(message: Message):
    await message.answer("Qaybiri haqida malumot olishni istaysiz ", reply_markup=menufriends)

@dp.message_handler(text='Izzat')
async def send_photo(message: Message):
    photo_id = "AgACAgIAAxkBAANNYSzVlicoSGeWFTJ2zU9s3N3TdlcAAi-1MRs8yGlJ4egtyjY2G7sBAAMCAAN5AAMgBA"
    await message.reply_photo(photo_id,caption="Pidaraz bola \nOdam bo'lishi juda qiyin Mansabparaz \nLaqabi: 'Xamelion'", reply_markup=menufriends)

@dp.message_handler(text='Islom')
async def send_photo(message: Message):
    photo_id = "AgACAgIAAxkBAAM5YSzPD73Dsny62RuCqrbnHyKvCNkAAiO1MRs8yGlJHEGXinX8rkkBAAMCAAN5AAMgBA"
    await message.reply_photo(photo_id, caption="Samimiy bola Big Bon kampaniyasi Asoschisi \nShou Biznes yulduzi \nO'zining unitilmas qo'shiqlari bilan tomoshabin qalbidan joy olgan", reply_markup=menufriends)

@dp.message_handler(text='Xabibullo')
async def send_link(message: Message):
    photo_id = "AgACAgIAAxkBAANFYSzS3MA9hUntbjJizP60feESU20AAiq1MRs8yGlJ5nCKFlJ4_4cBAAMCAAN5AAMgBA"
    await message.reply_photo(photo_id,caption="Amazon Asoschisi \nSeryozniy yurishi yoqtiralla \nJuda chuqur O'ylidila Yaqnda shu chuqurga o'zlari tushub ketadila " , reply_markup=menufriends)

@dp.message_handler(text='Jamshid')
async def send_link(message: Message):
    photo_id = "AgACAgIAAxkBAANLYSzUoNkFEDOUZYBK08QPcY8u_fEAAi21MRs8yGlJNw9RBzYCz08BAAMCAAN5AAMgBA"
    await message.reply_photo(photo_id,caption="Professor Xayolparas \nYordami ko'p tegadi \nMani ustozim \nLaqabi: 'Krakadil'", reply_markup=menufriends)

@dp.message_handler(text='Jamol')
async def send_link(message: Message):
    photo_id = "AgACAgIAAxkBAANHYSzTmRNq5w_dHjS8b4x9KdAFeHQAAiu1MRs8yGlJdtOezQUnmvABAAMCAAN4AAMgBA"
    await message.reply_photo(photo_id, caption="Bitcoin Asoschisi Satoshi Nakomoto \nJuda harakatchan bola \nLaqabi: 'Jumong','Tutqich bermas chumoli' ", reply_markup=menufriends)

@dp.message_handler(text='Ilyos')
async def send_link(message: Message):
    photo_id = "AgACAgIAAxkBAANDYSzSW86chxwcvgaEEeGx26JtSNUAAim1MRs8yGlJRxaTdkfpt1ABAAMCAAN4AAMgBA"
    await message.reply_photo(photo_id,caption="Butun dunyoni qogoz bilan taminlidi \nBurgani Ko'tini ko'rgan bola \nLaqabi: 'Akula'", reply_markup=menufriends)

@dp.message_handler(text='Ibrohim')
async def send_link(message: Message):
    photo_id = "AgACAgIAAxkBAANPYSzV3KhlzQAB2pTkWpf7JJ_BRai4AAIytTEbPMhpSb5CPuDQbomnAQADAgADeAADIAQ"
    await message.reply_photo(photo_id,caption="Media Park Asoschisi \nOdil bilan Nurini O'rtogi \nLaqabi: 'Suv mushugi'", reply_markup=menufriends)

@dp.message_handler(text='Shohjahon')
async def send_link(message: Message):
    photo_id = "AgACAgIAAxkBAANJYSzUJ_PIH83qgYhbzNV5-Pfg1kkAAiy1MRs8yGlJUqyliAKvw6sBAAMCAAN4AAMgBA"
    await message.reply_photo(photo_id, caption="Elektra set Direktori \nJuda aqlli aka Yaxshi maslahatla chiqadi \nYaqnda to'y bo'ladi ", reply_markup=menufriends)


@dp.message_handler(text='Log Out')
async def send_link(message: Message):
    await message.answer("Do'stlar haqida malumotlarni bilib Oldingiz", reply_markup=ReplyKeyboardRemove())