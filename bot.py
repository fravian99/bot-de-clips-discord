import os
import discord
from discord.ext import commands 
import my_token

# Establecer permisos por defecto
intents = discord.Intents.default()
# Activar permiso de leer el contenido de los mensages
intents.message_content = True
# Esto es para poner que los comandos tengan que ir precedidos de "!" y que los permisos sean los permisos (capacidad de explicacion 100 XD)
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    """
    Notifica cuando es activado (realmente es innecesario)
    """
    print("Bot activado")


@bot.command()
async def test(ctx, *, arg):
    """
    Comando test para probar que funcionan los comandos 
    """
    await ctx.send(arg)


@bot.command(name = "clips")
async def clips(ctx: commands.Context):
    """
    Comando que recopila los clips 
    """
    contains = "https://clips.twitch.tv/"
    LIMIT = 1000
    clips = []
    text = ""
    title = "Recopilatorio de clips\n"

    flag_file = False

    try:
        messages = [message async for message in ctx.channel.history(limit=LIMIT) if contains in message.content and message.reference is None]
    except Exception:
        raise Exception("Error recibiendo mensajes")
    
    print("Mensajes recopilados, separando enlaces de clips de twitch...")

    
    for message in messages:
        words = message.content.split()
        for word in words:
            if contains in word and word not in clips:
                clips.append(word)
                text += word + "\n"
    
    
    if len(title + text) >2000 or flag_file and text>0:
        print("Como no se puede mandar mas de 2000 caracteres, se enviara como archivo")
        with open ("clips.txt","w") as file:
            file.write(text)
        try:
            await ctx.reply(file=discord.File("clips.txt"), content= title)
        except Exception:
            raise Exception("Error al enviar")
    
    elif len(text) > 0: 
        text  = title + text
        await ctx.reply(content=text)
    
    print("Mensaje con link de clips enviado")
    
    

bot.run(my_token.my_token)
