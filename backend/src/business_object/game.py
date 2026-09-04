from datetime import datetime
from enum import Enum
from business_object.player import Player

class Game_mode_enum(Enum):
    COINFLIP="coinflip"
    DICE="DICE"

class Game:
    def __init__(
        self,
        p1 : Player,        
        p2 : Player,
        game_mode: str,
        winner=None,
        description: str = "",
        timestamp: datetime = None # type: ignore
    ):
        self.id_game = id
        self.p1 = p1
        self.p2 = p2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

    def __str__(self):
        winner_name = self.winner.username if self.winner else "Draw"

        return (
            f"{self.game_mode} between {self.p1.username} "
            f"and {self.p2.username}. Winner: {winner_name}"
        )
    