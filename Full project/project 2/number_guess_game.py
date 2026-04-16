import random

secret_number = random.randint(1, 500)
num_guesses = 0

while True:
    guess = int(input("Guess the number (1-500): "))
    num_guesses += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {num_guesses} attempts!")
        break  # This is the "emergency exit" for the infinite loop