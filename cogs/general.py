import discord
from discord import app_commands
from discord.ext import commands

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="test", description="Responds with Pong!")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

    @app_commands.command(name="clean", description="Borra mensajes del canal")
    @app_commands.describe(cantidad="Cantidad de mensajes a borrar")
    async def clean(self, interaction: discord.Interaction, cantidad: int):
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

    @app_commands.command(name="sync", description="Sync commands to this server (Admin only)")
    async def sync(self, interaction: discord.Interaction):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "Solo administradores pueden usar este comando.", ephemeral=True
            )
            return

        await interaction.response.defer(ephemeral=True)

        try:
            # Sync to current guild
            synced = await self.bot.tree.sync(guild=interaction.guild)
            await interaction.followup.send(
                f"✓ Sincronizados {len(synced)} comandos a este servidor.\n"
                f"Los comandos deberían aparecer ahora.",
                ephemeral=True
            )
        except Exception as e:
            await interaction.followup.send(
                f"✗ Error al sincronizar: {e}",
                ephemeral=True
            )

async def setup(bot):
    await bot.add_cog(GeneralCog(bot))
