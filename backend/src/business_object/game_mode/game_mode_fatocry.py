from typing import Literal

from .coinflip_mode import CoinFlipMode
from .dice_mode import DiceMode
from .game_mode import GameMode


class GameModeFactory:
    """
    Class to select a game mode.
    """

    @classmethod
    def get_mode(cls, game_mode: Literal["coinflip", "dice"]) -> GameMode:
        """
        Returns the corresponding GameMode object.
        Args:
            game_mode (Literal["coinflip", "dice"]): The identifier of the game mode (e.g., 'coinflip', 'dice').
        Returns:
            GameMode: An instance of a class implementing GameMode.
        """
        if game_mode == "coinflip":
            return CoinFlipMode
        else:
            return DiceMode
