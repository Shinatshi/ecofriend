import discord
from discord.ext import commands, tasks
import random
import asyncio
import requests 


CHANNEL_ID = 1273968538302025792
sovety = [
    "Используйте многоразовые сумки вместо пластиковых.",
    "Экономьте воду: выключайте кран, пока чистите зубы.",
    "Сортируйте отходы и сдавайте вторсырьё в переработку.",
    "Сократите использование одноразовой посуды и упаковки.",
    "Используйте энергосберегающие лампы и приборы.",
    "Не выбрасывайте электронику - сдавайте её в специальные пункты приёма.",
    "Используйте общественный транспорт, чтобы сократить выбросы углекислого газа.",
    "Уменьшите потребление мяса для снижения экологического следа.",
    "Поддерживайте местные фермерские рынки и производители.",
    "Используйте экопродукты для уборки дома и стирки."
]
napominania = [
    "Не забывай выключать свет.",
    "Используй многоразовые сумки.",
    "Сортируй мусор для переработки.",
    "Экономь воду при использовании.",
    "Покупай местные продукты.",
    "Используй многоразовые бутылки.",
    "Сокращай использование пластика.",
    "Выбирай экологичные моющие средства.",
    "Ходи пешком или на велосипеде.",
    "Покупай только необходимое."
]
facts = [
    "Один деревьев поглощает примерно 22 кг углекислого газа в год.",
    "Переработка алюминиевых банок экономит 95% энергии по сравнению с производством новых.",
    "Каждый год в океан попадает около 8 миллионов тонн пластика."
]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print('Бот запущен!')
    send_random_napominania.start()

@bot.command(name='sovet')
async def sovet(ctx):
    advice = random.choice(sovety)
    await ctx.send(advice)

@bot.command(name='fact')
async def fact(ctx):
     fact = random.choice(facts)
     await ctx.send(fact)


@tasks.loop(seconds=3600)
async def send_random_napominania():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        advice = random.choice(napominania)
        await channel.send(advice)
    else:
        print(f"Канал с ID {CHANNEL_ID} не найден.")




        

bot.run('-')