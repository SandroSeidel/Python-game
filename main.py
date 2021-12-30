import random 
import choice_parser
import os
import platform
import time

while True:
    
    #Verify the OS and executes the especific command to clear to terminal 
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

    print("### Let's play rock, paper, scissor ###")
    print("Keys to play: \n",
        "1 - Rock\n",
        "2 - Paper\n",
        "3 - scissor")
    ##1 == 'Pedra', 2 == 'Papel', 3 == 'Tesoura'

    machine_choice = random.randrange(1, 3)
    player_choice = None

    print("\nPlayer 1 is playing... ")
    
    while True:
        try:
            player_choice = int(input("Your move "))
            if player_choice < 1  or player_choice > 3:
                print("PLEASE USE ONLY THE MOVE KEYS")
            else:
                break
        except:
            print("PLEASE USE ONLY THE MOVE KEYS")
    
    #Evaluate the moves 
    result = choice_parser.Choice_Parser(player_choice, machine_choice)

    print("\nThe machine is playing...\n3")
    time.sleep(3)
    print("\nMachine move:\n\n", machine_choice)
    
    
    if result == 1:
        print("\n\nPLAYER 1 AS WON!\n\n")
    elif result == 2:
        print("\n\nPLAYER 2 AS WON!\n\n")
    elif result == 3:
        print("\n\nIT'S A TIE!\n\n")
        
    #break the main loop if the player wants to stop
    play_again = input("Want to play again? (y/n)")
    if play_again == 'n':
        break

    
    