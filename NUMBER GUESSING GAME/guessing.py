import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    name = input("Please enter your name: ")
    print(f"Hello, {name}! I'm thinking of a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while attempts < 10:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations, {name}! You guessed the number ({secret_number}) correctly in {attempts} attempts!")
                play_again()
                return  # Exit the function
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print(f"Game over! You ran out of attempts. The secret number was {secret_number}.")
    play_again()

def play_again():
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Game Over!")

# Start the game
play_game()
