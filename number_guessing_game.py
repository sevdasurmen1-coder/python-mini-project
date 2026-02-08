import random

number = random.randint(1,100)

count = 0
max_try = 5

print("Number Guessing Game")
print("I picked a number between 1 and 100.")
print("You have 5 valid attempts.\n")

while count < max_try:
    user_input = input("Guess a number(1-100):").strip()

    try:
        guess_number = int(user_input)
    
    except ValueError:
        print("Invalid input! Please enter a whole number(e.g.,7,42,100).\n")
        continue
    if not(1 <= guess_number <= 100):
        print("Out of range! Please enter a number between 1 and 100.\n")
        continue

    count += 1

    difference = abs(guess_number-number)

    if guess_number == number:
        print("Congratulations! You found the number:",number)
        print("Total attempts:",count)
        break

    if guess_number < number:
        direction_hint = "Higher!"
    else:
        direction_hint = "Lower!"

    if difference <= 5:
        temperature_hint = "Very hot!"
    elif difference <= 15:
        temperature_hint = "Warm!"
    else:
        temperature_hint = "Cold!"

    print(direction_hint,temperature_hint)
    print(f"Attempts left: {max_try -count}\n")

else:
    print("Game Over!")
    print("The correct number was:",number)

