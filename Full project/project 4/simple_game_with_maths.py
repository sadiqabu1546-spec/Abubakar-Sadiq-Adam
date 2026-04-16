import random
import math

def guessing_game():
    secret_number = random.randint(1, 1000)
    max_guesses = 12
    guesses_taken = 0
    last_guess = None

    while guesses_taken < max_guesses:
        guess_str = input("Guess a number between 1 and 100 (or type 'hint'): ")
        
        # Enhancement 2: Contextual Hints
        if guess_str.lower() == "hint":
            if last_guess is None:
                print("Make at least one guess first to get a contextual hint!")
            elif last_guess < secret_number:
                hints = ["It's higher than your last guess!", "Try adding 10 to your previous guess."]
                print(f"Here's a hint: {random.choice(hints)}")
            else:
                hints = ["It's lower than your last guess!", "Try subtracting 5 from your previous guess."]
                print(f"Here's a hint: {random.choice(hints)}")
            continue # Hints don't count as a guess here

        try:
            guess = int(guess_str)
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
            continue

        guesses_taken += 1
        last_guess = guess

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {guesses_taken} guesses!")
            break
        
        # Enhancement 1: Dynamic Hints with math
        if guesses_taken >= 3:
            sqrt_hint = math.floor(math.sqrt(secret_number))
            print(f"Hint: The integer part of the square root of the number is around {sqrt_hint}.")

    if last_guess != secret_number:
        print(f"Sorry, you ran out of guesses. The number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()
