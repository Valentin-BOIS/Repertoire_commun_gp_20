# uv run --project backend python backend/src/sandbox.py
from business_object.game import Game
from business_object.player import Player
from dao.game_dao import GameDao
from utils.env_variables import load_environment_variables
from datetime import datetime

load_environment_variables()   # Required to load the variables needed (env) to connect to the database 

p1 = Player(username="Toto", password="Toto12", elo="12", email="toto@gmail.com", pokemon_fan="TRUE")
p2 = Player(username="Tata", password="Tata12", elo="21", email="tata@gmail.com", pokemon_fan="FALSE")
game = Game(player1=p1, player2=p2, game_mode="dice", winner=p1, description="blabla", timestamp=datetime.now(), id_game = "45678")

id = GameDao().create(p1)
print(id)
game2 = GameDao().find_by_id(45678)