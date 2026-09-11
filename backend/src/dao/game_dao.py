from dao.player_dao import PlayerDao

from business_object.game import Game
from business_object.player import Player
from dao.db_connection import DBConnection
from utils.log_utils import get_logger, log
from utils.singleton import Singleton


class GameDao(metaclass=Singleton):

    @log
    def create(self, player) -> bool:
            """Create a game in the database.
            Args:
                game to create
            Returns:
                True if creation is successful, False otherwise
            """
            res = None

            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO game(player1, player2, game_mode, winner, description, timestamp, id_game) VALUES "
                            "(%(player1.id_player)s, %(player2.id_player)s, %(game_mode)s, %(winner.id_player)s, %(description)s, %(timestamp)s, %(id_game)s) "
                            "RETURNING id_game;",
                            {
                                "player1": game.player1,
                                "player2": game.player2,
                                "game_mode": game.game_mode,
                                "winner": game.winner,
                                "description": game.description,
                                "timestamp": game.timestamp,
                                "id_game": game.id_game,
                            },
                        )
                        res = cursor.fetchone()
            except Exception as e:
                logger.error(e)
                raise

            created = False
            if res:
                player.id_player = res["id_player"]
                created = True

            return created

    @log
    def find_by_id(self, id_game: int) -> Game:
        """Find a game by their id.
        Args:
            id_game (int): The ID of the game to find
        Returns:
            Game matching the given id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                            "
                        "  FROM game                       "
                        " WHERE id_game = %(id_game)s;   ",
                        {"id_game": id_game},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        game = None
        if res:
            game = Game(
                player1=PlayerDAO().find_by_id(res["player1"]),
                player2=PlayerDAO().find_by_id(res["player2"]),
                game_mode=res["game_mode"],
                winner=PlayerDAO().find_by_id(res["winner"]),
                description=res["description"],
                timestamp=res["timestamp"],
                id_game=res["id_game"],
            )

        return game
