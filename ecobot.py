import discord
from discord.ext import commands, tasks
import random
import asyncio
import requests 


CHANNEL_ID = Channelid

quotes = [
    "Земля — наш общий дом. Давайте заботиться о ней вместе.",
    "Изменения начинаются с каждого из нас.",
    "Маленькие шаги могут привести к большим переменам.",
    "Тот, кто заботится об экологии, заботится о будущем.",
    "Каждый день — шанс сделать мир лучше."
]

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

eco_questions = [
    {
        "question": "Сколько лет разлагается пластиковая бутылка?",
        "options": ["50 лет", "100 лет", "450 лет", "1000 лет"],
        "answer": 3
    },
    {
        "question": "Какое дерево наиболее эффективно поглощает углекислый газ?",
        "options": ["Береза", "Дуб", "Тополь", "Ель"],
        "answer": 2
    },
    {
        "question": "Какой процент мирового мусора составляют пластиковые отходы?",
        "options": ["10%", "30%", "50%", "70%"],
        "answer": 2
    }
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

@bot.command(name='quote')
async def quote(ctx):
    quote = random.choice(quotes)
    await ctx.send(quote)

@bot.command(name='quiz')
async def quiz(ctx):
    question_data = random.choice(eco_questions)
    question = question_data["question"]
    options = question_data["options"]
    correct_answer = question_data["answer"]
    options_str = "\n".join([f"{i+1}. {option}" for i, option in enumerate(options)])
    await ctx.send(f"{question}\n{options_str}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

    try:
        guess_msg = await bot.wait_for('message', check=check)
        guess = int(guess_msg.content)

        if guess == correct_answer:
            await ctx.send("Правильно! Отлично справился!")
        else:
            await ctx.send(f"Неверно. Правильный ответ: {options[correct_answer-1]}")
    except asyncio.TimeoutError:
        await ctx.send("Время вышло! Попробуй снова.")


@tasks.loop(seconds=3600)
async def send_random_napominania():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        advice = random.choice(napominania)
        await channel.send(advice)
    else:
        print(f"Канал с ID {CHANNEL_ID} не найден.")




        

bot.run('token)
