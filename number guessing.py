import random

number = random.randint(1, 100)
attempts = 5

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")
print("You have 5 attempts")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Congratulations! You guessed correctly!")
        break

    elif guess > number:
        print("Too high!")

    else:
        print("Too low!")

    attempts -= 1
    print("Remaining attempts:", attempts)

if attempts == 0:
    print("Game Over! The number was:", number)
