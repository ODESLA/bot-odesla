# Copyright 2020 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.

"""Example code for the nodes in the example pipeline. This code is meant
just for illustrating basic Kedro features.

Delete this when you start working on your own Kedro project.
"""
# pylint: disable=invalid-name

import logging
from typing import Any, Dict

import numpy as np
import pandas as pd
import discord
from discord.ext import commands
from mee6_py_api import API
import datetime

from .utils import LoadCredentials, ConnectDrive

from urllib import parse, request
import re

# Load Credentials
client = LoadCredentials()
credentials = client.credentials


def run_bot_odesla():

    bot = commands.Bot(command_prefix="!", description="Bot de ODESLA")

    @bot.command()
    async def info(ctx):
        embed = discord.Embed(
            title=f"{ctx.guild.name}",
            descripcion="Test",
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.blue(),
        )
        embed.add_field(name="1", value=f"{ctx.guild.created_at}")
        embed.add_field(name="2", value=f"{ctx.guild.created_at}")
        embed.add_field(name="3", value=f"{ctx.guild.created_at}")
        await ctx.send(embed=embed)

    @bot.command()
    async def ayuda(ctx):
        await ctx.send("Hola, podes usar los siguientes comandos en el chat:")
        await ctx.send("!iniciativas: Para acceder a la lista de iniciativas. ")
        await ctx.send("!colaborar: Si queres sumarte a los colaboradores.")
        await ctx.send("!web: Es nuestra web oficial.")
        await ctx.send("!git: Para acceder a nuestro repositorio de codigo.")
        await ctx.send("!rank: Para ver como estas rankeado segun tu participacion.")
        await ctx.send("!levels: Para ver el ranking con todos los participantes.")
        await ctx.send("Envianos tu consulta al canal #│🤔│consultas")

    @bot.command()
    async def web(ctx):
        embed = discord.Embed(
            title="Te invitamos a visitar nuestra web",
            url="https://www.odesla.org",
            descripcion="ODESLA - Comunidad de Cientificos de Datos Latinos",
            color=discord.Color.orange(),
        )
        await ctx.send(embed=embed)

    @bot.command()
    async def iniciativas(ctx):
        embed = discord.Embed(
            title="Iniciativas actuales en ODESLA",
            url="https://docs.google.com/spreadsheets/d/1b_rVXLIuktHJR3u5fEtH2nIswTUPeKaDdXPu6gLWjc0/edit?usp=sharing",
            description="En este documento están todas las iniciativas que vamos cargando. \
            Hay un identificador numérico (Numero en la primer columna) que te permite hacer consultas más fácilmente \
            en el canal #│🤔│consultas. Pega el identificador numérico junto a tu pregunta: Ejemplo: 2101001 - Quiero saber  \
            mas sobre la tarea del dashboad. \
            ¡Toda colaboración se agradece!",
            color=discord.Color.orange(),
        )
        await ctx.send(embed=embed)

    @bot.command()
    async def colaborar(ctx):
        embed = discord.Embed(
            title="Registrate acá",
            url="https://docs.google.com/forms/d/e/1FAIpQLSf-AOsILx4A3Xi_v_PInqQRD5pLFnvoH5zJR5asY-I_xc2KDA/viewform",
            description="En este doc podes inscribirte como colaborador, con ese registro pasas a ser parte de los \
            colaboradores de ODESLA. Una vez registrado, cambiaremos tus rol de discord a COLABORADOR y vas a poder acceder a un canal de \
            coordinación para ir avanzando en las iniciativas. Cualquier duda escribinos en #│🤔│consultas",
            color=discord.Color.orange(),
        )
        await ctx.send(embed=embed)

    @bot.command()
    async def git(ctx):
        await ctx.send("https://github.com/ODESLA")

    @bot.command()
    @commands.is_owner()
    async def shutdown(ctx):
        """async function to shutdown the bot"""
        await ctx.bot.logout()

    @bot.command()
    @commands.is_owner()
    async def save_leaderboard(ctx):
        """async function to save the MEE6 leaderboard into a google spreadsheet"""

        # Connect and retrieve information from MEE6 Leaderboard
        mee6api = API(credentials["bot_key"]["key_api"])
        leaderboard_page = await mee6api.levels.get_leaderboard_page(0)

        # Connect to Google Drive
        g_client = ConnectDrive()
        g_client.save_leaderboard(leaderboard_page)

        await ctx.send("Saved")

    bot.run(credentials["bot_key"]["key_bot"])


run_bot_odesla()
