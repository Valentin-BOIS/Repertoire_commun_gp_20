from abc import ABC, abstractmethod


class ScoringStrategy(ABC):

    @abstractmethod
    def compute(self, p1, p2, winner) -> tuple:
        """
        Calcule les scores des deux joueurs.

        Args:
            p1: Joueur 1
            p2: Joueur 2
            winner: Joueur gagnant ou None si égalité

        Returns:
            tuple: (score_p1, score_p2)
        """
        pass