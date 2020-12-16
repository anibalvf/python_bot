import discord

client = discord.Client()
#kRYhpLPLFZETxPLH7llPjbrqL9KeVYqv

@client.event
async def on_ready():
    general_channel = client.get_channel(277119530038198273)
    await general_channel.send("Entro en 1m")

@client.event
async def on_message(message):
    general_channel = client.get_channel(277119530038198273)
    if message.content == "que":
        await general_channel.send("QUEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    elif message.content.startswith("-borrar"):
        partes = message.content.split()
        if int(partes[1])<=10:
            await message.channel.purge(limit=int(partes[1]))
        else:
            await general_channel.send("no puedes borrar mas de 10 mensajes a la vez")



    

client.run("Nzg4NTgxOTg2NzI5ODUyOTU4.X9lmNA.TplXw5bFT9Cvj_teMVPJRFkH07c")

# client.close()
