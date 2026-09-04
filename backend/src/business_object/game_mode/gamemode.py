from abc import ABC, abstractmethod

from ..game import Game, Player


class GameMode(ABC):
    @abstractmethod
    def play(p1: Player, p2: Player) -> Game:
        pass
