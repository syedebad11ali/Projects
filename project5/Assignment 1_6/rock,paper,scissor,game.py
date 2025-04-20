import random as r

score = 0
c_score = 0

while True:
    game = ("rock", "paper", "scissor")
    computer=r.choice(game)
    user_input = input(f"Enter your choice from {game}: ").lower()
    user_choice=int(game.index(user_input))
    computer_choice=int(game.index(computer))
    if user_input not in game:  
        print("Invalid Input! Please enter rock, paper, or scissor.")
        continue  
    
    computer = r.choice(game)
    print(f"Computer chose: {computer}")

        
    if (user_choice-computer_choice)%3==1:
        score += 1
        print("You win!")
    elif user_input == computer:
        print("It's a draw!")
    else:
        c_score += 1
        print("You lose!")

    
    play = input("Do you want to play again? (y/n): ").lower()
    if play != "y":
        print(f"Final Score - You: {score}, Computer: {c_score}")
        break
    if play == "y":
        print(f"Final Score - You: {score}, Computer: {c_score}")
        continue

# Start the game
# game_in()
