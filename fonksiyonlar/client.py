import json

class BotHakkinda(object):
    def Prefix(self):
        with open("./ayarlar.json", "r") as f:
            data = json.load(f)
            return data["prefix"]

    def Token(self):
        with open("./ayarlar.json", "r") as f:
            data = json.load(f)
            return data["token"]

    def Developer(self):
        with open("./ayarlar.json", "r") as f:
            data = json.load(f)
            return data["developer"]