import random

print("=" * 40)
print("      NUMBER GUESSING GAME")
print("=" * 40)

secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7
print("I have selected a number between 1 and 100.")
print(f"You have {max_attempts} chances to guess it.\n")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low! Try a higher number. 🔽")
        elif guess > secret_number:
            print("Too High! Try a lower number. 🔼")
        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the correct number: {secret_number}")
            print(f"You took {attempts} attempts.")
            break
        print(f"Attempts left: {max_attempts - attempts}\n")
    except ValueError:
        print("Please enter a valid number!\n")

if attempts == max_attempts and guess != secret_number:
    print("\nGame Over! ❌")
    print(f"The correct number was: {secret_number}")