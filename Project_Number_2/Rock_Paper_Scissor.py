# Name : Syed Abuzar Tirmizi
#G-Mail: s.abuzartirmizi@gmail.com

import random
user_wins = 0

# Run the game for 3 rounds
for _ in range(3):
    while True:

        # Used .lower to turn capital letters to small
        user = input("Your Choice: Rock, Paper, Scissor:").lower()
        comp_options = ["rock", "paper", "scissor"]

        # Give error for wrong input 
        if user not in comp_options:
            print(f"{user} is not an option. Please choose again.")
        else:

            # Computer will print rondom choices 
            comp_choice = random.choice(comp_options)
            print("Computer's choice:", comp_choice)

            #  Checks user and computer choices  for output              
            if (comp_choice == user): 
                print("It's a Tie")
            elif (comp_choice == "rock") and (user == "scissor"):
                print("You Lose!")
            elif (comp_choice == "paper") and (user == "rock"):
                print("You lose!")
            elif (comp_choice == "scissor") and (user == "paper"):
                print("You lose!")
            elif (comp_choice == "scissor") and (user == "rock"):
                print("You Win!")

                # Add your points by 1, if you  won!
                user_wins += 1
            elif (comp_choice == "rock") and (user == "paper"):
                print("You Win!")
                user_wins += 1
            elif (comp_choice == "paper") and (user == "scissor"):
                print("You Win!")
                user_wins += 1

            # exit the while loop        
            break

#After 3 rounds it will output your wins in the string
print(f"Your wins are {user_wins} out of 3")