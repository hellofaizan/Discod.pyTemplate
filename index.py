# Code a slash command discord bot in python
import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix = 'c!', intents = discord.Intents.all())

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        self.synced = True
        print('Bot is ready')

bot = abot()
tree = app_commands.CommandTree(bot)

@tree.command(name = 'about', description = 'About the bot')
async def self(indentation: discord.Interaction):
    await indentation.response.send_message('I am a simple Discord.py 14 template to get started created a new Discord bot easily. Template made by <@890232380265222215>')

bot.run(os.getenv('TOKEN'))