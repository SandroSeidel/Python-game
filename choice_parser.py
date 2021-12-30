##That function will verify the moves and define the winner 
def Choice_Parser(player1_choice, player2_choice):
    ## Entry meanings
    ## 1 == "Rock"
    ## 2 == "Paper"
    ## 3 == "Scissor"
    
    ##Return meanings
    ## return 1 == the winner is player 1
    ## return 2 == the winner is player 2 
    ## return 3 == ia  a tie 
    
    if player1_choice == 1 and player2_choice == 1:
        return 3
    elif player1_choice == 1 and player2_choice == 2:
        return 2
    elif player1_choice == 1 and player2_choice == 3:
        return 1
        
    elif player1_choice == 2 and player2_choice == 1:
        return 1
    elif player1_choice == 2 and player2_choice == 2:
        return 3
    elif player1_choice == 2 and player2_choice == 3:
        return 2
        
    elif player1_choice == 3 and player2_choice == 1:
        return 2
    elif player1_choice == 3 and player2_choice == 2:
        return 1
    elif player1_choice == 3 and player2_choice == 3:
        return 3
        
