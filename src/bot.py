"""Customização da classe padrão do bot."""

import asyncio
from logging import getLogger
from random import shuffle

import discord
from discord import Game
from discord.ext.commands import Bot

discord.utils.setup_logging()
logger = getLogger(__name__)

lista_status: list[str] = [
    "Pico Celestial",
    "Mosteiro do Penhasco",
    "Ruínas Amaldiçoadas",
    "Salão da Bravura",
    "Laboratório Hextec",
    "Arena dos Desafiadores",
    "Docas da Matança",
]


class BotCustom(Bot):
    """Instância para guardar o escopo global do bot."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.indice_status: int = 0

    async def on_ready(self) -> None:
        await self.circular_status()

        logger.info("Bot iniciado com sucesso!")

    async def circular_status(self) -> None:
        """Alterna periodicamente entre os status do bot."""
        shuffle(lista_status)

        while True:
            if self.indice_status % len(lista_status) - 1 != 0:
                await self.change_presence(
                    activity=Game(lista_status[self.indice_status])
                )
                self.indice_status += 1

            else:
                shuffle(lista_status)
                self.indice_status = 0

            await asyncio.sleep(5)
