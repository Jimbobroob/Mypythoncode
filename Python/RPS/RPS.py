import random
import time


def main(): 
    print("Pick R P  or S")
    player_input = input("R P or S: ")
    rand = ['P','S', 'R']
    computer_choice = random.choice(rand)
    time.sleep(1)
    if player_input == 'R' and computer_choice == 'P':
        print("You Lose")
    elif player_input == 'R' and computer_choice == 'S':
        print("You Win")    
    elif player_input == 'R' and computer_choice == 'R':
        print("Tie")    
    elif player_input == 'P' and computer_choice == 'P':
        print("Tie")    
    elif player_input == 'P' and computer_choice == 'S':
        print("You Lose")    
    elif player_input == 'P' and computer_choice == 'R':
        print("You Win")    
    elif player_input == 'S' and computer_choice == 'P':
        print("You Win")    
    elif player_input == 'S' and computer_choice == 'S':
        print("Tie")    
    elif player_input == 'S' and computer_choice == 'R':
        print("You Lose")

    time.sleep(0.5)    
    print("The computer chose",computer_choice)
    print("You chose",player_input)
main()