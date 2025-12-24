import discord
from discord import app_commands
from discord.ext import commands
import os
import asyncio
from config import config

class MyClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.load_cogs()

        guild = discord.Object(id=config.GUILD_ID)
        await self.tree.sync(guild=guild)
        print(f"Synced commands to guild {config.GUILD_ID}")

    async def load_cogs(self):
        cogs_dir = os.path.join(os.path.dirname(__file__), 'cogs')
        for filename in os.listdir(cogs_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                cog_name = filename[:-3]
                try:
                    await self.load_extension(f'cogs.{cog_name}')
                    print(f'Loaded cog: {cog_name}')
                except Exception as e:
                    print(f'Failed to load cog {cog_name}: {e}')

client = MyClient()
client.run(config.TOKEN)