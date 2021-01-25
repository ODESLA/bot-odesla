import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='!', description="Bot de ODESLA")


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", 
    descripcion='Test',timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.blue())
    embed.add_field(name="1", value=f"{ctx.guild.created_at}")
    embed.add_field(name="2", value=f"{ctx.guild.created_at}")
    embed.add_field(name="3", value=f"{ctx.guild.created_at}")
    await ctx.send(embed=embed)

@bot.command()
async def ayuda(ctx):
    await ctx.send('Hola, podes usar los siguientes comandos en el chat:')
    await ctx.send('!colaborar: Si queres sumarte a los colaboradores.')
    await ctx.send('!iniciativas: Para acceder a la lista de iniciativas. ')
    await ctx.send('!web: Es nuestra web oficial.')
    await ctx.send('!git: Para acceder a nuestro repositorio de codigo.')
    await ctx.send('!rank: Para ver como estas rankeado segun tu participacion.')
    await ctx.send('!levels: Para ver el ranking con todos los participantes.')
    await ctx.send('Envianos tu consulta al canal #│🤔│consultas')


@bot.command()
async def web(ctx):
    embed = discord.Embed(title="Te invitamos a visitar nuestra web", 
    url="www.odesla.org",
    descripcion='ODESLA - Comunidad de Cientificos de Datos Latinos', 
    color=discord.Color.orange())
    await ctx.send(embed=embed)


@bot.command()
async def iniciativas(ctx):
    embed = discord.Embed(title="Iniciativas actuales en ODESLA", 
    url="https://docs.google.com/spreadsheets/d/1b_rVXLIuktHJR3u5fEtH2nIswTUPeKaDdXPu6gLWjc0/edit?usp=sharing",
    description='En este documento están todas las iniciativas que vamos cargando. \
        Hay un identificador numérico (Numero en la primer columna) que te permite hacer consultas más fácilmente \
        en el canal #│🤔│consultas. Pega el identificador numérico junto a tu pregunta: Ejemplo: 2101001 - Quiero saber  \
        mas sobre la tarea del dashboad. \
        ¡Toda colaboración se agradece!',
    color=discord.Color.orange())
    await ctx.send(embed=embed)

@bot.command()
async def colaborar(ctx):
    embed = discord.Embed(title="Registrate acá", 
    url="https://docs.google.com/forms/d/e/1FAIpQLSf-AOsILx4A3Xi_v_PInqQRD5pLFnvoH5zJR5asY-I_xc2KDA/viewform",
    description='En este doc podes inscribirte como colaborador, con ese registro pasas a ser parte de los \
        colaboradores de ODESLA. Una vez registrado, cambiaremos tus rol de discord a COLABORADOR y vas a poder acceder a un canal de \
        coordinación para ir avanzando en las iniciativas. Cualquier duda escribinos en #│🤔│consultas',
    color=discord.Color.orange())
    await ctx.send(embed=embed)

@bot.command()
async def git(ctx):
    await ctx.send('https://github.com/ODSL-oficial')

#Events
async def on_ready():
    print('READY')

bot.run('ODAyNTc3ODk1MjU0OTE3MTQy.YAxQ6Q.si00ItXmvZcXoeGFdK8NAMAYAMA')