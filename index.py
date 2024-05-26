BOT_PREFIX = "PREFİX GİRİNİZ"
BOT_TOKEN = "TOKEN GİRİNİZ"
WELCOME_CHANNEL_ID =WELCOME KANAL İD GIR
LEAVE_CHANNEL_ID =LEAVE KANAL İD GIR
import discord
import random
import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
      

      print ('_________________________________________')
      print ('Developer          : Chany')
      print ('Language           : discord.py = Python')
      print ('Version            : 0.0.1')
      print ('Durum              : Aktif')
      print(bot.user.name , '   : Kullanıcı Adıyla Giriş Yapıldı')
      print(bot.user.id , ': İd İle Giriş Yapıldı')
      print ('_________________________________________')

      await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Developed Chany'))

@bot.event
async def on_member_join(member):
    try:
        channel = bot.get_channel(WELCOME_CHANNEL_ID)
        try:
            embed = discord.Embed(colour=discord.Colour.green())
            embed.set_author(name=member.name, icon_url=member.avatar_url)
            embed.add_field(name='Hoş Geldin', value=f"**Hey,{member.mention}  `{member.guild.id}` ! Sunucuya Katıldı**", inline=False)
            embed.set_thumbnail(url=member.guild.icon_url)
            embed.set_footer(text=footer)
            await channel.send(embed=embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e

@bot.event
async def on_member_remove(member):
    try:
        channel = bot.get_channel(LEAVE_CHANNEL_ID)
        try:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=member.name, icon_url=member.avatar_url)
            embed.add_field(name='Görüşürüz', value=f"**{member.mention} `{member.guild.id}` Sunucudan ayrıldı**", inline=False)
            embed.set_thumbnail(url=member.guild.icon_url)
            embed.set_footer(text=footer)
            await channel.send(embed=embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e
footer = 'Developed Chany'
@bot.command()  // KOMUT LOADER 
async def load(ctx, extension):
    bot.load_extension(f'Cog.{extension}')
 
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'Cog.{extension}')

for filename in os.listdir("./Cog"):
    if filename.endswith('.py'):
        bot.load_extension(f'Cog.{filename}[:-3]')


bot.run(BOT_TOKEN)
