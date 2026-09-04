from abc import ABC, abstractmethod
import datetime


class GameMode(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def game(self, player1, player2):
        """
        Lance une partie et retourne le gagnant.
        Retourne None en cas d'égalité.
        """
        pass
    
class DiceMode(GameMode):

    def __init__(self):
        super().__init__("dice")

    def game(self, p1, p2):
        import random
        score1 = random.randint(1, 6)
        score2 = random.randint(1, 6)

        if score1 > score2:
            winner = p1
        elif score2 > score1:
            winner = p2
        else:
            winner= None
        return Game(p1,p2,GameMode_enum.DICE,winner,desc,datetime.now())