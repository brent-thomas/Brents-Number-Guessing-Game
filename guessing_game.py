import random
import statistics
import math

# Display Welcome Message
def welcome_message():
    print("-" * 36)
    print("Welcome to Brent's Number Guessing Game!")
    print(" * I'm thinking of a number between 1 and 100.")
    print(" * If your guess is too high or too low, I'll let you know. :)")
    print(" * Good luck!")
    print("-" * 36)

#Print the high score if there are any previous attempts
def print_high_score(scores):
    if len(scores) > 0 :
        high_score = min(scores)
        print(f'See if you can beat the high score, {high_score}\n')


#Check to see if the guess is correct and provide feedback to the user
def check_guess(guess, solution):
    if guess >=1 and guess <=100:
        if guess > solution:
            return "It's lower"
        elif guess < solution:
            return "It's higher"
    else:
        return "Uh oh, that's outside the range. The secret number is between 1 and 100. Try again."
    
#Display end of game message, disply score statistics, and prompt player to play again
def end_of_game_sequence(solution,number_of_attempts,scores):
        print('*' * 36)
        print(f"\nBe you angels!? You got it! The correct number was {solution}\n")
        print(f"You got it right in {number_of_attempts} attempts")
        print("\nHigh Score Statistics:\n")
        print(f'Mean: {statistics.mean(scores)}')
        print(f'Median: {statistics.median(scores)}')
        print(f'Mode: {statistics.mode(scores)}')
        print()
        print('*' * 36)
        return input("Would you like to play again? [Y/N] ")

def start_game():
    welcome_message()
    scores = []
    while True:
        number_of_attempts = 0
        guess = 0
        solution = random.randint(1,100)
        print_high_score(scores)
        while guess != solution:
            try:
                
                guess = int(input("Make a guess: "))
                number_of_attempts +=1
                print(check_guess(guess,solution))
            except ValueError:
                print("Please enter a valid whole number")
        scores.append(number_of_attempts)
        play_again = end_of_game_sequence(solution,number_of_attempts,scores)
        if play_again.upper() == 'Y':
            print("\nGreat! I've picked a new number.How many attempts will it take you this time?\n")
            continue
        else:
            print("\nGoodbye for now!\n\n**Self Destructing in 3,2,1...\n\n")
            break

start_game()