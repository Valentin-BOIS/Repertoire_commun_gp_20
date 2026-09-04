from datetime import datetime
from enum import Enum

from .player import Player


class Game_mode_enum(Enum):
    COINFLIP = "coinflip"
    DICE = "dice"


class Game:
    """
    Class representing a Game.
    Attributes:
        id_game (int) : identifiant du game,
        player1 (Player) : le premier joueur du game,
        player2 (Player) : le second joueur du game,
        game_mode (Literal["coinflip", "dice"]) : mode de jeu, qui ne peut etre que lancer de des ou jet de de,
        winner (Player | None) : vainqueur de la partie, qui peut etre non renseigne en cas de partie nulle,
        description (str) : informations supplementaires sur le game,
        timestamp (datetime) : temps
    """

    def __init__(
        self,
        player1: Player,
        player2: Player,
        game_mode: Game_mode_enum,
        winner: [Player | None],
        description: str,
        timestamp: datetime,
        id_game: [int | None] = None,
    ):
        """Constructor"""
        self.id_game = id_game
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

    def __str__(self):
        """Returns a string representation of the game.
        Returns:
            str: A string containing the username and Elo rating.
        """
        return f"{self.game_mode} between {self.player1.username} and {self.player2.username})"
