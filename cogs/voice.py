import discord
from discord import app_commands
from discord.ext import commands
from utils.audio import AudioUtils

class VoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"VoiceCog loaded and ready!")

async def setup(bot):
    @bot.tree.command(name="speak", description="convert text to audio", guild=discord.Object(id=1310814995013046315))
    @app_commands.describe(texto="Ingresa el texto que dirá el bot")
    async def speak(interaction: discord.Interaction, texto: str):
        if not interaction.user.voice:
            await interaction.response.send_message(
                "Debes estar en un canal de voz.", ephemeral=True
            )
            return

        channel = interaction.user.voice.channel
        await interaction.response.send_message("🔊 Hablando...", ephemeral=True)

        vc = interaction.guild.voice_client

        if vc is None:
            vc = await channel.connect()
        elif vc.channel != channel:
            await vc.move_to(channel)
            
        audio_file = await AudioUtils.generate_tts_audio(texto)

        try:
            await AudioUtils.play_audio_in_voice_channel(vc, audio_file)
        finally:
            AudioUtils.cleanup_audio_file(audio_file)

    await bot.add_cog(VoiceCog(bot))
    print("VoiceCog setup completed with manual command registration")