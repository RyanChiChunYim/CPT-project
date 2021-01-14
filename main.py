import random

def main() :
  print("\tWELCOME TO THE STONKS! This is a more turn based game filled with comedy and fun!")

print("How to play.")
print("There will be decisions that you will need to make")
print(" (Note: Moves can miss, including Heal(Move is called Taco Bell MEGA Doritos Queserito!)")

print("\nEach player starts with 100 health")
print("Who ever reaches the health of 0 loses")
print("\nLETS PLAY ")

play_game = True

while play_game :
  winner = None
  health_player = 100
  health_opponent = 100

  turn = random.randint (1,2)
  if turn == 1 :
    player_turns = True
    opponent_turns = False
    print ("The human will proceed immediately ")
  else :
    player_turns = False
    opponent_turns = True
    print ("The opponent will proceed immediately")

print ("\nPlayer health: ", health_player, "Opponent health: ", health_opponent)

while (health_player != 0 or health_opponent != 0) :
  heal = False
  miss_move = False

  player_moves = {"the baby punch": random.randint (1,11),
                  "mEgA kIcc": random.randint (11,21),
                  "MUDA MUDA MUDA" : random.randint (25, 26),
                  "心臓を捧げよ!" : random.randint (5,10),
                  "Truck-Kun!" : random.randint (26,41),
                  "Taco Bell MEGA Doritos Queserito" : random.randint (25, 31), }
  if player_turns :
    print ("\nSelect one of the moves:\n1. the baby punch\n2.mEgA kIcc\n3.MUDA MUDA MUDA\n4.心臓を捧げよ!\n5.Truck-Kun!\n6. Taco Bell MEGA Doritos Queserito ")
    





                  
