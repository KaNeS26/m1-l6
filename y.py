import discord
from discord.ext import commands
import os, random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Você logou como {bot.user}')

@bot.command()
async def info(ctx):
    await ctx.send('Hello, im recicle bot!, im here to help you with your recycling needs!  I can help you to recicle the materials you have at home by the right way.Currently, I can help you with the following materials: Paper, Plastic, Glass and Metal,just type "!<material>" to get the information you need!')
      
@bot.command()
async def paper(ctx):
    await ctx.send('Paper can be recycled at the blue bin. Its one of the most common materials that can be recycled, and also important due to the ways it is used, which means an increase in the demand for paper. Dont waste it, recicle it!'
    'For more information about paper recycling, you can check the following link: https://www.ecycle.com.br/reciclagem-de-papel/')

@bot.command()
async def plastic(ctx):
    await ctx.send('Plastic can be recycled at the red bin. Its one of the most used materials in the world, and also one of the most harmful to the environment. Dont throw it away in any place, recicle it and help the nature!'
                   'For more information about plastic recycling, you can check the following link:https://trevoreciclagem.com.br/como-reciclar-plastico-tudo-o-que-voce-precisa-saber-para-fazer-certo/')

@bot.command()
async def glass(ctx):
    await ctx.send('Glass can be recycled at the green bin. Its one of the most impressive materials that can be recycled, and also one of the most beautiful materials used in the world. Dont you think that its a shame to throw it away by any place? Recicle it and turn glass into a new glass!'
                   'For more information about glass recycling, you can check the following link: https://www.ype.ind.br/ype-explica/como-reciclar-vidro')

@bot.command()
async def metal(ctx):
    await ctx.send('Metal can be recycled at the yellow bin. Its one of the most versatile materials that can be recycled, and also one of the most valuable to the environment. Dont throw it away like a normal item, it is very useful and can stay in nature for over 100 years, recicle it!'
                   'For more information about metal recycling, you can check the following link: https://recykloo.com.br/descarte-e-reciclagem-de-metais/')

bot.run(TOKEN)