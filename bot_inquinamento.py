import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def buongiorno(ctx):
    await ctx.send(f'buongiorno, come stai?')

@bot.command()
async def bene(ctx):
    await ctx.send(f'mi fa piacere,\U0001f642')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def sottrazione(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def moltiplicazione(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def divisione(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left % right)

@bot.command()
async def leggi(ctx):
    with open('text.txt', 'r', encoding='utf-8') as f:
       # print(f.read())
       await ctx.send(f.read())

@bot.command()
async def scrivi(ctx):
    with open('text.txt', 'w', encoding='utf-8') as f:
        text = "bho"
        f.write(text)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)    
        await ctx.send(file = picture)

@bot.command()
async def mem2(ctx):
    img_name = random.choice(os.listdir('images2'))
    with open(f'images2/{img_name}', 'rb') as f:
        picture = discord.File(f)    
        await ctx.send(file = picture)

@bot.command()
async def inquinamento(ctx):
    img_name = random.choice(os.listdir('images_inquinamento'))
    with open(f'images_inquinamento/{img_name}', 'rb') as f:
        picture = discord.File(f)    
        await ctx.send(file = picture)





bot.run("inserisci il tuo token qui!)
