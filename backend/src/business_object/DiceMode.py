import random
from business_object.GameMode import GameMode

class DiceMode(GameMode):

    def __init__(self):
        super().__init__("dice")

    def play(self, player1, player2):
        score1 = random.randint(1, 6)
        score2 = random.randint(1, 6)

        if score1 > score2:
            print("le score1 vaut", score1, " et le score2 vaut", score2)
            return player1
        
        elif score2 > score1:
            print("le score2 vaut", score2, " et le score1 vaut", score1)
            return player2
        else:
            print("Les deux scores sont ", score1)

            return None


p1 = "Jacky"

p2 = "Jackie"

dice_mode = DiceMode()

game = dice_mode.play(p1, p2)

print(game)