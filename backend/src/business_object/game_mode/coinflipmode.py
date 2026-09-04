import datetime
import secrets

from ..game import Game, Player
from .gamemode import GameMode


class DiceMode(GameMode):
    def play(p1: Player, p2: Player, choice: str = "heads") -> Game:
        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2

        return Game(
            player1=p1,
            player2=p2,
            game_mode="coinflip",
            winner=winner,
            description=None,
            timestamp=datetime.now(),
        )
