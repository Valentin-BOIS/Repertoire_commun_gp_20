import secrets
from datetime import datetime

from ..game import Game
from ..player import Player
from .game_mode import GameMode


class DiceMode(GameMode):
    """
    Class representating a dice game.
    """

    def play(p1: Player, p2: Player) -> Game:
        """
            Simulate a dice game.

        Attributs:
            p1 (Player): The first player to play.
            p2 (Player): The second player to play.
        """
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
            description=f"{p1.username}: {d1}, {p2.username}: {d2}"
            + (f"{winner.username} won" if winner is not None else "draw"),
            timestamp=datetime.now(),
        )
