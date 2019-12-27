import random

x = False


def drop():
    return random.randint(1, 6)


while bool(x) is not True:
    print("") if x is None else print("None")
    print("Random numbers is: ", drop(), "and", drop())
    print("Input text or keep empty: ")
    x = input()

