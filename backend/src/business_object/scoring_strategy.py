import os

from .game import Game


class ScoringStrategy:
    """
    Class representing the strategy methode.
    """

    @classmethod
    def calculate_expected_score(cls, game: Game) -> float:
        """Calculates the probability of player A winning against player B.
        Args:
            game (Game): The game that leads to elo update.
        Returns:
            float: The expected score for player 1 (between 0 and 1).
        """
        elo_a = game.player1.elo()
        elo_b = game.player2.elo()
        return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))

    @classmethod
    def calculate_new_ratings(cls, game: Game) -> tuple[int, int]:
        """Computes the new Elo ratings for two players after a match.
        Args:
            game (Game): The game that leads to elo update.
        Returns:
            tuple[int, int]: A tuple containing (new_elo1, new_elo2).
        """
        k_factor = int(os.environ["ELO_K_FACTOR"])

        score_a = 1.0 if game.winner() == game.player1() else 0.0
        score_b = 1.0 - score_a

        elo_a = game.player1.elo()
        elo_b = game.player2.elo()
        new_elo_a = round(elo_a + k_factor * (score_a - cls.calculate_expected_score(elo_a, elo_b)))
        new_elo_b = round(elo_b + k_factor * (score_b - cls.calculate_expected_score(elo_b, elo_a)))

        return new_elo_a, new_elo_b

    @classmethod
    def update_player_ratings(cls, game: Game) -> None:
        """Calculates and updates the elo attributes of the players.
        No update if there is no winner (Draw).
        Args:
            game (Game): The game that leads to elo update.
        """
        winner = game.winner()
        if winner is None:
            return

        p1 = game.player1()
        p2 = game.player2()
        p1.elo, p2.elo = cls.calculate_new_ratings(p1.elo, p2.elo, player_a_won=(p1 == winner))
        return
