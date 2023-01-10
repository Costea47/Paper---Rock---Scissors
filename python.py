import random, os
from art import draw

choices = ["rock" , "paper" , "scissors"]

def determine_winner(player, opp):
    # Check if its a tie
    if player == opp:
        return("It's a tie game!")
    # Check if the player won
    elif ((player == "rock" and opp == "scissors") or
          (player == "paper" and opp == "rock") or
          (player == "scissors" and opp == "paper") ):
            return ("You won, congratulations!")
    # If they didn't win, then we know they lost
    else:
        return("You lost, sorry!")

playing, invalid = True, False

while playing:
    if not invalid:
        # Ask the player to make a selection 
        # Let them know if their previous choice was invalid
        print("Choose rock, paper or scissors")
    else:
        print("Invalid input, please type rock,paper or scissors")
        invalid = False
        print("Or enter q to quit")
        # Get the player input, make it lowercase and remove white spaces

    player_choice = input().lower().strip()
    # Generate a random choice for the computer

    opp_choice = random.choice(choices)
    #Check and see if the player made a valid entry

    if player_choice in choices:
        print("You chose: "+ player_choice + draw(player_choice))
        print("The opponent chose: "+ opp_choice + draw(opp_choice))
        print(determine_winner(player_choice, opp_choice))
    # End the loop if the player wants to leave

    elif player_choice == 'q':
        playing = False

    else:
        invalid = True
    
    # The iteration of the game is done, ask to play again

    if playing and not invalid:
        replay = input("Wanna play again?\nType \"yes\" to replay\nEnter anything else to end the game\n").lower().strip()
        print()
        playing = replay == "yes"

        # Clear the screen

        os.system('cls' if os.name == 'nt' else 'clear')

    print("Thanks for playing!")