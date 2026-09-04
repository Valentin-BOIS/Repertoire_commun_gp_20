from GameMode import GameMode
from CoinFlipMode import CoinFlipMode
from DiceMode import DiceMode


class GameModeFactory:

    @classmethod
    def get_mode(cls, game_mode: str) -> GameMode:
        """
        Returns the corresponding GameMode object.

        Args:
            game_mode (str): The identifier of the game mode
                            (e.g., "coinflip", "dice").

        Returns:
            GameMode: An instance of a class implementing GameMode.

        Raises:
            ValueError: If the requested game_mode is not supported.
        """

        if game_mode.lower() == "coinflip":
            return CoinFlipMode()

        if game_mode.lower() == "dice":
            return DiceMode()

        raise ValueError(f"Unsupported game mode: {game_mode}")