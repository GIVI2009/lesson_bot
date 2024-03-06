import asyncio
import logging
import random

from decouple import config


from aiogram import Bot, Dispatcher, Router, types,F
from aiogram.utils import keyboard
from aiogram.filters import CommandStart, Command   


TOKEN = config("TOKEN")

dp = Dispatcher() 
bot = Bot(TOKEN)




dictionary = {
    "cats": [
    'https://www.cats.org.uk/media/13136/220325case013.jpg?width=500&height=333.49609375',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTX1qpHC87QFvtWIrs9bP1wTpQyC_H9nke2XJO_n5kwG4WhJL7imwcHtysq5-Ow1ctcjhg&usqp=CAU',
    'https://www.purina.co.uk/sites/default/files/2023-03/Hero%20Pedigree%20Cats.jpg',
    'https://static.scientificamerican.com/sciam/cache/file/2AE14CDD-1265-470C-9B15F49024186C10_source.jpg?w=1200',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUzdyfZ-Omq_LDifJ31U7YfqsRlxYEMs-eQVSoFXcz1A&s',
    'https://flomaster.top/uploads/posts/2023-01/1673455960_flomaster-club-p-kotik-v-shapochke-lyagushki-risunok-krasiv-1.jpg',
    'https://oboi-telefon.ru/wallpapers/128886/36379.jpg'
    ],
    "dogs": [
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYyqT3NT0KtDdrkXj-FjDXocU0BZ-O-nZpTvskLpKS-g&s',
        'https://sobakovod.club/uploads/posts/2022-02/1644748113_1-sobakovod-club-p-sobaki-krasivie-sobak-v-khoroshem-kachestv-1.jpg',
        'https://w.forfun.com/fetch/43/430012d695ee75291fd7502fd49f458a.jpeg',
        'https://cdn.royalcanin-weshare-online.io/3CENa2QBaxEApS7Lqd5j/v6/yellow-labrador-lying-in-the-grass',
        'https://bogatyr.club/uploads/posts/2023-03/1679132677_bogatyr-club-p-sobaka-v-temnote-foni-krasivo-1.jpg',
        'https://klike.net/uploads/posts/2019-06/1559799842_1.jpg',
        'https://klike.net/uploads/posts/2023-02/1675491407_3-48.jpg'
    ],
    "capybaras": [
        'https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Hydrochoeris_hydrochaeris_in_Brazil_in_Petr%C3%B3polis%2C_Rio_de_Janeiro%2C_Brazil_09.jpg/800px-Hydrochoeris_hydrochaeris_in_Brazil_in_Petr%C3%B3polis%2C_Rio_de_Janeiro%2C_Brazil_09.jpg',
        'https://i.pinimg.com/564x/c5/cb/ff/c5cbff1b7efbfa2fe60ab1e12cda8899.jpg',
        'https://www.meme-arsenal.com/memes/699a19f76473bdc887f6775858fb3f1a.jpg',
        'https://pbs.twimg.com/media/FHVz87BXEAE4JmZ.jpg:large',
        'https://i.pinimg.com/564x/fc/9b/db/fc9bdbb1c8c4697c82fde291371b05bb.jpg',
        'https://i.pinimg.com/564x/1a/64/a1/1a64a149df1562307fc1274e2ebe1a04.jpg'
    ],
    "ilends": [
        'https://img.hotels24.ua/photos/ria/new_images/1123/112316/11231689/11231689m.jpg',
        'https://cheapfortrip.com/blog/app/uploads/2022/07/gettyimages-927861108-1380x690-1-1024x512.jpg',
        'https://ethnomir.ru/upload/medialibrary/b20/ocean1.jpg',
        'https://www.onetwotrip.com/ru/blog/static/images/10-most-beautiful-islands-for-summer-holidays/sea-coron-philippines.jpg',
        'https://vokrugsveta.ua/wp-content/uploads/2017/01/love-island-desktop-background-high-definition-wallpaper.jpg',
        'https://planetofhotels.com/guide/sites/default/files/styles/node__blog_post__bp_banner/public/2021-07/Murter.jpeg',
        'https://images.lucentcms.com/iyc_website/2020/12/5fea07e8729e2-caribbean-luxury-yacht-charter-min.jpg'
    ]
}



# клавиатура с кнопками

# kb_builder = keyboard.ReplyKeyboardBuilder()
# kb_builder.button(text = "Пес_random_photo")
# kb_builder.button(text = "Остров_random_photo")
# третья кнопака и четвёртая
# ну и надо ещё в старт добавить активацию 2-4 кнопок 
# для бабушек🤣

@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")

@dp.message(Command("help"))
async def maybe_help(message: types.Message):
    await message.answer("бро ты можешь написать кот, cat, кошка, кіт, кішка ")
    await message.answer("также можно собака, Пёс, dog, цуцик, цуцення")
    await message.answer("или ilend, остров, острів, островок")
    await message.answer("и фоворит capybaras, капибара, Чил, капібара, какібара, какибара")




@dp.message()
async def send_random_animal_picture(message: types.Message):
    text = message.text.lower()
    if any(keyword in text for keyword in ["кот", "cat", "кошка", "кіт", "кішка"]):
        random_cats_index = random.randint(0, len(dictionary["cats"]) - 1)
        random_cats_link = dictionary["cats"][random_cats_index]
        await bot.send_photo(message.chat.id, random_cats_link)
        await message.answer("вот кошка")
    elif any(keyword in text for keyword in ["собака", "Пёс", "dog", "цуцик", "цуцення"]):
        random_dogs_index = random.randint(0, len(dictionary["dogs"]) - 1)
        random_dogs_link = dictionary["dogs"][random_dogs_index]
        await message.answer("вот собака")
        await bot.send_photo(message.chat.id, random_dogs_link)
    elif any(keyword in text for keyword in ["ilend", "остров", "острів", "островок"]):
        random_ilends_index = random.randint(0, len(dictionary["ilends"]) - 1)
        random_ilends_link = dictionary["ilends"][random_ilends_index]
        await bot.send_photo(message.chat.id, random_ilends_link)
        await message.answer("вот острова жаль разработщик долго не будет их владельцем")
    elif any(keyword in text for keyword in ["capybaras", "капибара", "Чил", "капібара", "какібара","какибара"]):
        random_capybaras_index = random.randint(0, len(dictionary["capybaras"]) - 1)
        random_capybaras_link = dictionary["capybaras"][random_capybaras_index]
        await bot.send_photo(message.chat.id, random_capybaras_link)
        await message.answer("капибара капибара какибар какибара...")
    else:
        await message.answer("Неизвестное животное")




# можно это через текст сделать но не абязательно есть много разных способов 
# @dp.message(F.text == 'Остров_random_photo')
# async def send_cat_picture(message: types.Message):
#     random_ilends_index = random.randint(0, len(dictionary["ilends"]) - 1)
#     random_ilends_link = dictionary["ilends"][random_ilends_index]
#     await bot.send_photo(message.chat.id, random_ilends_link)


# @dp.message(F.text == 'Пес_random_photo')
# async def send_cat_picture(message: types.Message):
#     random_dog_index = random.randint(0, len(dictionary["dogs"]) - 1)
#     random_dog_link = dictionary["dogs"][random_dog_index]
#     await bot.send_photo(message.chat.id, random_dog_link)
# .......





# я пробовал через айди но как оказалось через сылки легче чтоб повысить шанс на высокую оценку я использовал дикшенори для url на фото 
# @dp.message()
# async def echo_handler(message: types.Message):
#     print(message.photo)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())