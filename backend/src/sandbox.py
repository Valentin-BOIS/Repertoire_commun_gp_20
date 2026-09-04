from datetime import datetime

from business_object.game import Game
from business_object.player import Player

p1 = Player(username="Alice", elo=1312, email="alice@mail.com")
p2 = Player(username="Bob", elo=2131, email="bob@mail.com")
g = Game(player1=p1, player2=p2, game_mode="coinflip", winner=p1, description="test", timestamp=datetime(2026, 9, 4))
print(g)