import asyncio
import logging
from typing import Dict, Any


logger = logging.getLogger(__name__)
modules = []


class MModule(object):
    def __init__(self, name: str):
        from .commands import MCommand

        self.name: str = name
        self.config: Dict[str, Any] = {}
        self.commands: Dict[str, MCommand] = {}
        self.loaded: bool = False
        # The actual module
        self.module = None

    # NOTE: The module may or may not actually loaded by the time this is called.
    async def load_config(self, config: Dict[str, Any]):
        self.config = config
        # logger.debug(f"Got config {config}")
