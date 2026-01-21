import discord
from discord import app_commands
from discord.ext import commands
import os
import asyncio
from config import config

class MyClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.voice_states = True  # Enable voice state events
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.load_cogs()

        # Sync globally for all servers
        try:
            synced = await self.tree.sync()
            print(f"✓ Synced {len(synced)} commands globally")
            print(f"⚠️  Global commands may take up to 1 hour to appear in all servers")
            print(f"   Use /sync command in each server for instant sync")
        except Exception as e:
            print(f"✗ Failed to sync globally: {e}")

    async def load_cogs(self):
        cogs_dir = os.path.join(os.path.dirname(__file__), 'cogs')
        for filename in os.listdir(cogs_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                cog_name = filename[:-3]
                try:
                    await self.load_extension(f'cogs.{cog_name}')
                    print(f'✓ Loaded cog: {cog_name}')
                except Exception as e:
                    print(f'✗ Failed to load cog {cog_name}: {e}')

client = MyClient()
client.run(config.TOKEN)