import discord
import os
import sys
import traceback

from discord.ext import commands
from main import client

# burası eventleri tutacağımız kısım.
class Dinleyiciler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(">>> Kategoriler Yükleniyor...")

        # komut yükleme
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                filename = file[:-3]
                if filename in ["Dinleyiciler", "Hatalar"]: continue
                if filename.startswith("."): # eğer bir kategoriyi görmezden gelmesini isterseniz dosyanın başına . koydurabilirsiniz, kolaylık sağlaması için eklendi.
                    print(">>> Kategori: {0} Görmezden Gelindi.".format(file))
                    continue

                try:
                    client.load_extension("cogs.{0}".format(filename))
                    print(">>> Kategori: {0} Yüklendi.".format(filename))
                except Exception as error:
                    print(">>> Kategori: {0} Yüklenemedi.".format(filename))
                    # kapanmaması için hatayı print ettiriyoruz:
                    error = getattr(error, 'original', error)
                    print('>>> Kategoride Hata Var ({0}):'.format(filename), file=sys.stderr)
                    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        print(">>> Bot Hazır!")

    @commands.Cog.listener()
    async def on_message(self, message):
        # event deneme kısmı için oluşturulmuş basit bir örnek:
        if "sa" in message.content.lower():
            await message.reply("as")


def setup(client):
    client.add_cog(Dinleyiciler(client))
