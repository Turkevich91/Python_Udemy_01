import random

x = False

while bool(x) is not True:
    print("") if x is None else print("None")
    print(f"Random numbers is: {random.randint(1, 6)} and {random.randint(1, 6)}")
    print("Input text or keep empty: ")
    x = input(x)

