# uv run --project backend python backend/src/sandbox.py
from business_object.game import Game
from business_object.player import Player
from dao.game_dao import GameDao
from utils.env_variables import load_environment_variables

load_environment_variables()   # Required to load the variables needed (env) to connect to the database 

p1 = Player(...)
p2 = Player(...)
game = Game(...)

id = GameDao().create(...)
print(id)
game2 = GameDao().find_by_id(...)
