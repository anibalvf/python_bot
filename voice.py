import key
import discord
from discord.ext import commands
import youtube_dl
import os
import random
import time
from discord import FFmpegPCMAudio
from discord.utils import get


client = commands.Bot(command_prefix="!")

# # Setting `Playing ` status # await bot.change_presence(activity=discord.Game(name="a game"))

# # Setting `Streaming ` status # await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# # Setting `Listening ` status # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# # Setting `Watching ` status # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

@client.event
async def on_ready():
    actividad = discord.Game(name="Te rieh?")
    general_channel = client.get_channel(277119530038198273)
    await general_channel.send("te rieh? ya he llegado")
    await client.change_presence(status=discord.Status.idle,activity=actividad)


@client.command()
async def que(ctx):
    await ctx.send("QUEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")



@client.command()
async def shisha(ctx):
    eleccion = ["YEAAAH","YEAAAH"]
    await ctx.send("Decidiendo shisha rejuvenecedora")
    time.sleep(1)
    await ctx.send("3")
    time.sleep(1)
    await ctx.send("2")
    time.sleep(1)
    await ctx.send("1")
    time.sleep(1)

    resultado = random.choice(eleccion)
    
    embed = discord.Embed(title="HAY SHISHA?",description=resultado,color=0xff0000)
    embed.set_author(name="Anibal")
    await ctx.send(embed=embed)
    if resultado =="YEAAAH":
        if ctx.author.voice==None:
            await ctx.send("No puedes escuchar la respuesta conectate a un canal devoz")
        else:
            try:
                channel = ctx.author.voice.channel
                await channel.connect()
                voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            except:
                voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio("audios/guycoughing.mp3"))  
    


@client.command()
async def dominos(ctx):
    eleccion = ["YEAAAH","JAMAS"]

    await ctx.send("Decidiendo dominos en la maquina que da vueltas")
    time.sleep(1)
    await ctx.send("3")
    time.sleep(1)
    await ctx.send("2")
    time.sleep(1)
    await ctx.send("1")
    time.sleep(1)

    resultado = random.choice(eleccion)
    
    embed = discord.Embed(title="DOMINOS?",description=resultado,color=0xff0000)
    embed.set_author(name="Anibal")
    await ctx.send(embed=embed)

    if resultado =="JAMAS":
        if ctx.author.voice==None:
            await ctx.send("No puedes escuchar la respuesta conectate a un canal devoz")
        else:
            try:
                channel = ctx.author.voice.channel
                await channel.connect()
                voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            except:
                voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio("audios/guycoughing.mp3"))    



@client.command()
async def insultame(ctx):
    insultos = ["Gandúl","Comeflores","Capullo","Cernícalo","Comebolsas","Huevón","Hijo de puta","Inutil","Homo","Dario el cenizo"]

    # down()
    await ctx.message.author.send("Eres un "+random.choice(insultos))

@client.command()
async def borrar(ctx):
    partes = ctx.message.content.split()
    if int(partes[1])<=10:
        await ctx.channel.purge(limit=int(partes[1]))
    else:
        await ctx.send("no puedes borrar mas de 10 mensajes a la vez")

def down():
    url="https://www.youtube.com/watch?v=rS9VRg-TOgM"
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "guycoughing.mp3")    

@client.command(pass_context=True)
async def test(ctx):

    if ctx.author.voice==None:
        await ctx.send("Jamas no estas conectado a un canal de voz")
    else:
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        except discord.ClientException:
            await client.say('ya estoy en un canal')    

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        print("error")
        return
    try:
        if ctx.author.voice==None:
            await ctx.send("Jamas no estas conectado a un canal de voz")
        else:
            try:
                channel = ctx.author.voice.channel
                await channel.connect()
                voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            except discord.ClientException:
                voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
    except:
        print("ERROR! ME CAGO EN LA PUTA")



@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("No estoy conectado a ningun canal te rieh?")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("que vas a pausar si no hay musica payaso Dario el cenizo")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("tu puta madre ha quitado la pausa")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


client.run(key.getKey())