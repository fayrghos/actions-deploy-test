"""Gerenciamento de variáveis de ambiente."""

import logging
from os import getenv

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

if not load_dotenv():
    logger.warning("Nenhum arquivo .env foi encontrado!")

TOKEN_BOT: str = getenv("TOKEN_BOT", "")
if not TOKEN_BOT:
    logger.critical("Nenhum token foi passado ao bot.")
    exit(1)
