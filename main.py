import random


def main():
    """The main function that will welcome the player to the game(STONKS)."""

    print("\tWELCOME TO THE STONKS! This is a more turn based game filled with comedy and fun!  You must defeat the virus that is messing with your stonks and information!!!!!!")

    print("How to play.")
    print("There will be decisions that you will need to make")
    print(" (Note: Moves can miss, including Heal(Move is called Taco   Bell MEGA Doritos Queserito!)")

    print("\nEach player starts with 100 health")
    print("Who ever reaches the health of 0 loses")
    print("\nLETS PLAY ")


    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 100
        computer_health = 100

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails 50% Chance of heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nThe player will proceed immediately ")
        else:
            player_turn = False
            computer_turn = True
            print("\n The computer virus will proceed immediately")


        print("\nPlayer health: ", player_health, "Computer Virus health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            moves = {"The baby punch": random.randint(1, 11),
                     "mEgA kIcc": random.randint(10, 20),
                     "MUDA MUDA MUDA" : random.randint (30,35),
                     "心臓を捧げよ!" : random.randint (5,10),
                     "Truck-Kun!" : random.randint (26,41),
                     "Taco Bell MEGA Doritos Queserito": random.randint(25, 31)}

            if player_turn:
                print ("\nSelect one of the moves:\n1. the baby punch\n2.mEgA kIcc\n3.MUDA MUDA MUDA\n4.心臓を捧げよ!\n5.Truck-Kun!\n6. Taco Bell MEGA Doritos Queserito ")

                player_move = input("> ").lower()

               
               
               
                move_miss = random.randint(2,5) # 20% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                
                
                
                
                if miss:
                    player_move = 0 # player misses and deals no damage
                    print("haha you missed! L")
                else:
                    if player_move in ("1", "the baby punch"):
                        player_move = moves["the baby punch"]
                        print("\nYou used the baby punch! You big baby! Use something else! It dealt ", player_move, " damage.")
                    elif player_move in ("2", "mEgA kIcc"):
                        player_move = moves["mEgA kIcc"]
                        print("\nYou used mEgA kIcc. N i c e! It dealt ", player_move, " damage.")
                    elif player_move in ("3", "MUDA MUDA MUDA") :
                        player_move = moves["MUDA MUDA MUDA"]
                        print("\MUDA MUDA MUDA MUDA MUDA! It dealt ", player_move, " damage.")
                    elif player_move in ("4", "心臓を捧げよ!") :
                        player_move = moves ["心臓を捧げよ!"]
                       print ("\n You used 心臓を捧げよ! You just scream! Little damage done! It dealt ",player_move, "damage") 
                    elif player_move in ("5", "Truck-Kun!") :
                        player_move = moves ["Truck_Kun!"]
                        print ("\nYou used Truck-Kun! Most powerful antagonist in all of anime! It dealt",player_move, "damage")
                    elif player_move in ("6", "heal"):
                        heal_up = True # heal activated
                        player_move = moves["Taco Bell MEGA Doritos Queserito"]
                        print("\nYou used Taco Bell MEGA Doritos Queserito. It healed for ", player_move, " health.")
                    else:
                        print("\nWHAT ARE YOU DOING! THAT IS NOT A VALID MOVE LOL!")
                        continue

            
            
            else: # computer turn

                move_miss = random.randint(1,5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("Even the computer can miss!")
                else:
                    if computer_health > 30: 
                        if player_health > 70:
                            computer_move = moves["the baby punch"]
                            print("\nThe computer used the baby punch!. It dealt ", computer_move, " damage.")
                        elif player_health > 35 and player_health <= 70: # computer decides whether to go big or go home
                            imoves = ["mEgA kIcc", "MUDA MUDA MUDA", "心臓を捧げよ!", "Truck-Kun!",]
                            imoves = random.choice(imoves)
                            computer_move = moves[imoves]
                            print("\nThe computer used ", imoves, ". It dealt ", computer_move, " damage!")
                        elif player_health <= 35:
                            computer_move = moves["MUDA MUDA MUDA"] # FINISH THAT LOSER!!!!
                            print("\nThe computer used MUDA MUDA MUDA! It dealt ", computer_move, " damage.")                       
                    
                    
                    else: # if the computer has less than 30 health, there is a 50% chance they will heal
                        heal_or_fight = random.randint(1,2) 
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = moves["Taco Bell MEGA Doritos Queserito"]
                            print("\nThe computer used Taco Bell MEGA Doritos Queserito. It healed for ", computer_move, " health.")
                        
                        
                        
                        else:
                            if player_health > 75:
                                computer_move = moves["mEgA kIcc"]
                                print("\nThe computer used mEgA kIcc. It dealt ", computer_move, " damage.")
                            elif player_health > 35 and player_health <= 75:
                                imoves = ["the baby punch", "mEgA kIcc", "MUDA MUDA MUDA", "心臓を捧げよ!", "Truck Kun", ]
                                imoves = random.choice(imoves)
                                computer_move = moves[imoves]
                                print("\nThe computer used ", imoves, ". It dealt ", computer_move, " damage.")
                            elif player_health <= 35:
                                computer_move = moves["Truck-Kun!"] # FINISH THAT LOSER!
                                print("\nThe computer used Truck-Kun!. It dealt ", computer_move, " damage.")

            
            
            if heal:
                if player_turn:
                    player_health += player_move
                    if player_health > 100:
                        player_health = 100 # cap max health at 100. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 100:
                        computer_health = 100
            
            
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 0:
                        computer_health = 0 # cap minimum health at 0
                        winner = "The Player!"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Computer Virus!"
                        break

            
            
            
            print("\nPlayer health: ", player_health, "Computer Virus health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

        
        
        
        
        
        if winner == " The Player":
            print("\nPlayer health: ", player_health, "Computer Virus health: ", computer_health)
            print("\n Wow you just won! N-not like I would congratulate you or anything b-b-baka! \n Aftermath: Your stonks and information were not stolen form your computer and you can live rent free!")
        else:
            print("\nPlayer health: ", player_health, "Computer Virus health: ", computer_health)
            print("\nWow You just lost! Congrats! All your stonks and information is stolen and put on the black market! ._.")

        print("\nWould you like to play again?")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            play_again = False

main()
