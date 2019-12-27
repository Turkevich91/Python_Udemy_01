import random

x = False


def drop():
    return random.randint(1, 6)


while bool(x) is not True:
    print("") if x is None else print("None")
    print("Random numbers is: ", drop(), "and", drop())
    # print(f"Random numbers is: {random.randint(1, 6)} and {random.randint(1, 6)}")
    print("Input text or keep empty: ")
    x = input()

