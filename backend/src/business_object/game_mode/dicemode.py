import datetime
import secrets

from ..game import Game, Player
from .gamemode import GameMode


class DiceMode(GameMode):
    def play(p1: Player, p2: Player) -> Game:
        d1 = secrets.choice(range(1, 7))
        d2 = secrets.choice(range(1, 7))
        if d1 > d2:
            winner = p1
        elif d1 < d2:
            winner = p2
        else:
            winner = None
        return Game(
            player1=p1,
            player2=p2,
            game_mode="dice",
            winner=winner,
            description="",
            timestamp=datetime.now(),
        )
