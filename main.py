import os
# ayarlar.json doldurmayı unutmayınız.
# şuanki hali ile çalışır, ama klasör bulunamadı tarzı birşey söylerse:
# os.chdir("bot lokasyonu") ekleyebilirsiniz.

import discord
import sys
import traceback
from discord.ext import commands

from fonksiyonlar.client import BotHakkinda

client = commands.AutoShardedBot(command_prefix=BotHakkinda().Prefix(), intents=discord.Intents.all(), shard_count=1, cached_messages=50)
# intentleri açın, açmak istemiyorsanız "intents=discord.Intents.all()," kısmını silin
# cached messages daha az ram kullanımı için, istemiyorsanız kaldırabilirsiniz

try:
    client.load_extension("cogs.Dinleyiciler")
    client.load_extension("cogs.Hatalar")
    print(">>> Dinleyiciler ve Hatalar Yüklendi.")
except Exception as error:
    error = getattr(error, 'original', error)
    print('>>> Hata Var:', file=sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

client.run(BotHakkinda().Token())
