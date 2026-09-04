from datetime import datetime
from typing import Literal

from .player import Player


class Game:
    """
    Class representing a game.
    Attributs:
        id_game (int): The unique identifier for the game.
        player1 (Player): The first player of the game.
        player2 (Player): The second player of the game.
        game_mode (str): A game mode among 'coinflip' and 'dice'.
        winner (Player | None): The winner of the game, 'None' if draw.
        description (str): further details about the game.
        timestamp (datetime): La date du match.
    """

    def __init__(
        self,
        player1: Player,
        player2: Player,
        game_mode: Literal["coinflip", "dice"],
        winner: Player | None,
        description: str,
        timestamp: datetime,
    ) -> None:
        """Constructor"""
        self.id_game = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp
        return

    def __str__(self) -> str:
        """Returns a string representation of the game.
        Returns:
            str: A string containing the game mode, the two players and the winner of the game.
        """
        return f"{self.game_mode} between {self.player1.username} and {self.player2.username}. Winner : {self.winner.username}"
