import discord
from discord.ext import commands

MasterName = 'Hardrack'

class Saludos(commands.Cog):
    def __init__(self, HK47_bot):
        self.HK47_bot = HK47_bot

    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        await self.HK47_bot.change_presence(status=discord.Status.idle, activity=discord.Game('Star Wars: Knights of the Old Republic'))
        print('{0.user} is ready for duty, Master'.format(self.HK47_bot))

    # Commands
    @commands.command()
    async def info(self, ctx):
        self.embed = discord.Embed(title="Bot HK-47 para Discord", description="Mi creador es Hardrack#0150. Fui creado usando Python.", color=discord.Color.blue())
        self.embed.set_thumbnail(url="https://vignette2.wikia.nocookie.net/swtor/images/9/98/Swtor_2014-01-27_19-28-53-57.png/revision/latest?cb=20140127175759")

        await ctx.channel.send(embed=self.embed)

    @commands.command()
    async def hola(self, ctx):
        if ctx.author == self.HK47_bot.user:
            return

        if ctx.author.name == MasterName:
            await ctx.channel.send('Saludos Cordiales: Hola, Master!')
        else:
            await ctx.channel.send('Saludo: Hola, Bolsa de Carne!')

    @commands.command()
    async def adios(self, ctx):
        if ctx.author == self.HK47_bot.user:
            return

        if ctx.author.name == MasterName:
            await ctx.channel.send('Despedida solenme: Feliz descanso, Master!')
        else:
            await ctx.channel.send('Despedida: Adiós, Bolsa de Carne!')

def setup(HK47_bot):
    HK47_bot.add_cog(Saludos(HK47_bot))