import key
import discord
from discord.ext import commands
import youtube_dl
import os


client = commands.Bot(command_prefix="!")


# # Setting `Playing ` status
# await bot.change_presence(activity=discord.Game(name="a game"))

# # Setting `Streaming ` status
# await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# # Setting `Listening ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# # Setting `Watching ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

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
async def borrar(ctx):
    partes = ctx.message.content.split()
    if int(partes[1])<=10:
        await ctx.channel.purge(limit=int(partes[1]))
    else:
        await ctx.send("no puedes borrar mas de 10 mensajes a la vez")   


@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("me cago en mi puta madre ERROR")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='GRUPO1')
    await voiceChannel.connect()
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