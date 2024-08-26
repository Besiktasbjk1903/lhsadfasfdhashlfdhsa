from flask import Flask
from threading import Thread
from discord.ext import commands
import discord

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

# Jouw bot code hier...

keep_alive()  # Zorg ervoor dat de webserver actief blijft
bot.run("JOUW_DISCORD_BOT_TOKEN")
