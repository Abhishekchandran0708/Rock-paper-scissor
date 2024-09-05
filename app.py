# Rock Paper Scissors game in Python

import random

def play_game():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
        if user_choice == 'q':
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"\nComputer chose: {computer_choice}")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == 'rock':
            if computer_choice == 'scissors':
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_choice == 'paper':
            if computer_choice == 'rock':
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_choice == 'scissors':
            if computer_choice == 'paper':
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

play_game()
