from business_object.game import Game
from dao.db_connection import DBConnection
from dao.player_dao import PlayerDao
from utils.log_utils import get_logger, log
from utils.singleton import Singleton

logger = get_logger(__name__)


class GameDao(metaclass=Singleton):
    """Class containing methods to access Game in the database."""

    @log
    def create(self, game: Game) -> bool:
        """Create a game in the database.
        Args:
            Game to create
        Returns:
            True if creation is successful, False otherwise
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO game(id_player1, id_player2, game_mode, id_winner, detail) VALUES "
                        "(%(id_player1)s, %(id_player2)s, %(game_mode)s, %(id_winner)s, %(detail)s) "
                        "RETURNING id_game;",
                        {
                            "id_player1": game.id_player1,
                            "id_player2": game.id_player2,
                            "game_mode": game.game_mode,
                            "id_winner": game.id_winner,
                            "detail": game.detail,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        created = False
        if res:
            game.id_game = res["id_game"]
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
                id_game=res["id_game"],
                player1=PlayerDao().find_by_id(res["id_player1"]),
                player2=PlayerDao().find_by_id(res["id_player2"]),
                game_mode=res["game_mode"],
                winner=PlayerDao().find_by_id(res["id_winner"]),
                description=res["detail"],
                timestamp=res["timestamp"]
            )

        return game

    @log
    def find_all_by_player(id_player: int) -> list[Game]:
        """Find all the games played by a player.
        Args:
            id_player (int): The ID of the player to find the games.
        Returns:
            List of the games played by the player.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_game                            "
                        "  FROM game                       "
                        " WHERE id_player1 = %(id_player)s          "
                        " OR id_player2 = %(id_player)s  ;   ",
                        {"id_player": id_player},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logger.error(e)
            raise

        games = []
        if res:
            for id in res["id_game"]:
                games.append(GameDao.find_by_id(id))

        return games
