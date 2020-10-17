import discord
import random
from discord.ext import commands

MasterName = 'Hardrack'

class Juegos(commands.Cog):
    def __init__(self, HK47_bot):
        self.HK47_bot = HK47_bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send(f'pong! {round(self.HK47_bot.latency * 1000)}ms')

    @commands.command(aliases=['pregunta'])
    async def juegoDePregunta(self, ctx, *, question):
        respuestasPlebe = ['Es cierto, Bolsa de Carne.',
                    'Definitivamente, Bolsa de Carne.',
                    'Sin duda, Bolsa de Carne.',
                    'Si, definitivamente, Bolsa de Carne.',
                    'Si, Bolsa de Carne.',
                    'Pregunta después, Bolsa de Carne.',
                    'Mejor no te digo ahora, Bolsa de Carne.',
                    'La respuesta es no, Bolsa de Carne.',
                    'Mis fuentes dicen que no, Bolsa de Carne.',
                    'No, no va a pasar, Bolsa de Carne.',
                    'No, Bolsa de Carne.']

        respuestasMaster = ['Es cierto, Master.',
                    'Definitivamente, Master.',
                    'Sin duda, Master.',
                    'Si, definitivamente, Master.',
                    'Si, Master.',
                    'Pregunta después, por favor, Master.',
                    'Mejor no te digo ahora, Master.',
                    'La respuesta es no, Master.',
                    'Mis fuentes dicen que no, Master.',
                    'No, lo siento, Master.',
                    'No, Master.']

        if ctx.author.name == MasterName:
            await ctx.send(f'Pregunta: {question}\nRespuesta: {random.choice(respuestasMaster)}')
        else:
            await ctx.send(f'Pregunta: {question}\nRespuesta: {random.choice(respuestasPlebe)}')

def setup(HK47_bot):
    HK47_bot.add_cog(Juegos(HK47_bot))