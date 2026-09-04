from abc import ABC, abstractmethod

from ..game import Game
from ..player import Player


class GameMode(ABC):
    """
    Class representating a game mode.
    """

    @abstractmethod
    def play(p1: Player, p2: Player) -> Game:
        """
            Simulate a game.

        Attributs:
            p1 (int): The first player to play.
            p2 (int): The second player to play.
        """
        ...
