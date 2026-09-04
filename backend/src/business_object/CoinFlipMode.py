import random

from GameMode import GameMode
from Game import Game


class CoinFlipMode(GameMode):

    def __init__(self):
        super().__init__("coinflip")

    def play(self, p1, p2, choice) -> Game:
        """
        choice : 'heads' ou 'tails'
        """

        result = random.choice(["heads", "tails"])

        # Détermination du gagnant
        if choice == result:
            winner = p1
            loser = p2
        else:
            winner = p2
            loser = p1

        game = Game(
            player1=p1,
            player2=p2,
            game_mode="coinflip",
            winner=winner,
            description=f"Coin flip result: {result}. {winner.username} won."
        )

        return game