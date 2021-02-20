import discord
import os
import sys
import traceback

from discord.ext import commands
from main import client

# burası hataları yakalayacağımız kısım.
class Hatalar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        print('Komut ({0}) Hata Yakalandı:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(client):
    client.add_cog(Hatalar(client))
