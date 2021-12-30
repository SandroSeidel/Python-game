import random 
import choice_parser
import os
import platform

while True:

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

    print("Player 1 is playing: ")
    
    while True:
        try:
            player_choice = int(input("Your move "))
            if player_choice < 1  or player_choice > 3:
                print("PLEASE USE ONLY THE MOVE KEYS")
            else:
                break
        except:
            print("PLEASE USE ONLY THE MOVE KEYS")
    
    result = choice_parser.Choice_Parser(player_choice, machine_choice)
    print("Machine move:", machine_choice)
    
    if result == 1:
        print("PLAYER 1 AS WON!")
    elif result == 2:
        print("PLAYER 2 AS WON!")
    elif result == 3:
        print("IT'S A TIE!")
        
    play_again = input("Want to play again? (y/n)")
    if play_again == 'n':
        break

    
    