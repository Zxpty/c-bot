# C-Bot

My first Discord Bot

## Features

- **Test Command**: Simple ping-pong test command
- **Speak Command**: Text-to-speech functionality in voice channels
- **Clean Command**: Bulk message deletion with permission checks

## Project Structure

```
c-bot/
├── main.py              # Bot entry point
├── config.py            # Configuration and environment variables
├── requirements.txt     # Python dependencies
├── env_local.env        # Environment variables (not in git)
├── cogs/                # Discord cogs for organizing commands
│   ├── __init__.py
│   ├── general.py       # General commands (test, clean)
│   └── voice.py         # Voice-related commands (speak)
└── utils/               # Utility modules
    ├── __init__.py
    └── audio.py         # Audio processing utilities
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create `env_local.env` file with your Discord bot token:
   ```
   KEY=your_discord_bot_token_here
   ```

3. Run the bot:
   ```bash
   python main.py
   ```

## Adding New Features

### Adding a New Cog

1. Create a new file in the `cogs/` directory (e.g., `music.py`)
2. Implement your cog class inheriting from `discord.Cog`
3. Add an `async def setup(bot)` function at the end
4. The bot will automatically load all cogs from the `cogs/` directory

### Adding Utility Functions

Add utility functions to the `utils/` directory. Import them in your cogs as needed.

### Configuration

Add new configuration variables to `config.py` using environment variables for sensitive data.

## Commands

- `/test` - Responds with "Pong!"
- `/speak <text>` - Converts text to speech in voice channel
- `/clean <amount>` - Deletes specified number of messages (requires manage messages permission)