import discord
from discord import app_commands
from discord.ext import commands

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    
    @bot.tree.command(name="test", description="Responds with Pong!", guild=discord.Object(id=1310814995013046315))
    async def test(interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

    
    @bot.tree.command(name="clean", description="Borra mensajes del canal", guild=discord.Object(id=1310814995013046315))
    @app_commands.describe(cantidad="Cantidad de mensajes a borrar")
    async def clean(interaction: discord.Interaction, cantidad: int):
        if not interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message(
                "No tienes permisos para borrar mensajes.", ephemeral=True
            )
            return

        if cantidad < 1 or cantidad > 100:
            await interaction.response.send_message(
                "La cantidad debe estar entre 1 y 100.", ephemeral=True
            )
            return

        await interaction.response.defer(ephemeral=True)

        deleted = await interaction.channel.purge(limit=cantidad + 1)

        await interaction.followup.send(
            f"Se han borrado {len(deleted) - 1} mensajes.", ephemeral=True
        )

    await bot.add_cog(GeneralCog(bot))
    print("GeneralCog setup completed with manual command registration")