import random

x = False
limit = 6


def drop():
    return random.randint(1, limit)


while bool(x) is not True:
    print("") if x is None else print("None")
    print("Random numbers is: ", drop(), "and", drop())
    print("Input text or leave empty: ")
    x = input()

