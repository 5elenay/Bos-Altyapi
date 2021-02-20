import discord
from discord.ext import commands

from main import client

# her kategoride yeni bir cogs açıcaksınız.
class Deneme(commands.Cog, description="Genel komutlar için ayrılmış kategori."):
    def __init__(self, client):
        self.client = client

    @commands.command(description="Deneme için ping komutu", aliases=["ms"])
    async def ping(self, ctx):
        await ctx.reply(f"Pong, {round(client.latency * 1000)}ms")

def setup(client):
    client.add_cog(Deneme(client))
