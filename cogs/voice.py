import discord
from discord import app_commands
from discord.ext import commands
from utils.audio import AudioUtils

class VoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="speak", description="Convert text to audio")
    @app_commands.describe(texto="Ingresa el texto que dirá el bot")
    async def speak(self, interaction: discord.Interaction, texto: str):

        await interaction.response.defer(ephemeral=True)

        if not interaction.user.voice:
            await interaction.edit_original_response(
                content="Debes estar en un canal de voz."
            )
            return

        channel = interaction.user.voice.channel
        vc = interaction.guild.voice_client

        if vc is None:
            vc = await channel.connect()
        elif vc.channel != channel:
            await vc.move_to(channel)

        audio_file = await AudioUtils.generate_tts_audio(texto)

        try:
            await AudioUtils.play_audio_in_voice_channel(vc, audio_file)
            await interaction.edit_original_response(content="🔊 Hablando...")
        finally:
            AudioUtils.cleanup_audio_file(audio_file)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        """Event listener for voice state updates (joins, leaves, moves)."""
        # Check if user joined a voice channel
        if after.channel is not None and (before.channel is None or before.channel != after.channel):
            # Don't greet the bot itself
            if member.bot:
                return

            # Check if bot is already in a voice channel in this guild
            vc = member.guild.voice_client

            # Connect to the voice channel if not already there
            if vc is None:
                vc = await after.channel.connect()
            elif vc.channel != after.channel:
                await vc.move_to(after.channel)

            # Generate and play the greeting message
            greeting_text = "I'm Alex Valle 2, pleasure to know you"
            audio_file = await AudioUtils.generate_tts_audio(greeting_text, lang="en")

            try:
                await AudioUtils.play_audio_in_voice_channel(vc, audio_file)
            finally:
                AudioUtils.cleanup_audio_file(audio_file)

async def setup(bot):
    await bot.add_cog(VoiceCog(bot))
