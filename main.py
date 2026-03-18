"""O coração do bot."""

import discord

from src.bot import BotCustom
from src.envs import TOKEN_BOT


def main() -> None:
    intents = discord.Intents.default()
    intents.message_content = True

    bot = BotCustom(intents=intents, command_prefix="./")
    bot.run(token=TOKEN_BOT, log_handler=None)


if __name__ == "__main__":
    main()
