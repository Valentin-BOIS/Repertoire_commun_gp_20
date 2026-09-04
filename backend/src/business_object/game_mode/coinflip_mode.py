import secrets
from datetime import datetime
from typing import Literal

from ..game import Game
from ..player import Player
from .game_mode import GameMode


class CoinFlipMode(GameMode):
    """
    Class representating a coinflip game.
    """

    def play(p1: Player, p2: Player, choice: Literal["heads", "tails"] = "heads") -> Game:
        """
            Simulate a dice game.

        Attributs:
            p1 (Player): The first player to play.
            p2 (Player): The second player to play.
            choice (Literal["heads", "tails"]): The choice of the first player, 'heads' by default.
        """
        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2
        return Game(
            player1=p1,
            player2=p2,
            game_mode="coinflip",
            winner=winner,
            description="",
            timestamp=datetime.now(),
        )
