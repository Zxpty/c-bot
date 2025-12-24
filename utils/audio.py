import os
from gtts import gTTS
import discord
import asyncio

class AudioUtils:
    @staticmethod
    async def generate_tts_audio(text: str, lang: str = "es") -> str:
        """Generate TTS audio file and return the filename."""
        filename = "tts_output.mp3"
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(filename)
        return filename

    @staticmethod
    async def play_audio_in_voice_channel(vc: discord.VoiceClient, audio_file: str):
        """Play audio in voice channel and wait for completion."""
        audio = discord.FFmpegPCMAudio(audio_file)
        vc.play(audio)

        while vc.is_playing():
            await asyncio.sleep(0.5)

        vc.stop()

    @staticmethod
    def cleanup_audio_file(filename: str):
        """Remove the audio file after use."""
        if os.path.exists(filename):
            os.remove(filename)