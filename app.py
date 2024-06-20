import random

# Define the choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

# Main code to run the game
if __name__ == "__main__":
    play_game()