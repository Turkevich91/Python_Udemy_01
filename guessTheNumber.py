import random

value = None
guess = None
winCounter = 0
counter = 0

print("To win in this game you have to guess 3 times in a row")
print("What range for win do you want to have?")
attempts = int(input())


while winCounter < 3:
    value = random.randint(1, attempts)
    print(f"\nPut number between 1 and {attempts}: ")
    guess = int(input())
    counter += 1

    if value == guess:
        winCounter += 1
        print("Well done!")
    else:
        winCounter = 0
        print("Sorry, I guessed: ", value)

print("\nCongratulation!!!")
print("\nTo win in this game it taken you", counter, "steeps!")

