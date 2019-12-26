import random

x = 0
counter = 0


def drop():
    return random.randint(1, 6)


while x <= 2:
    counter += 1
    map(drop, a, b)
    # a = drop()
    # b = drop()
    if a == b:
        x += 1
        if x >= 1:
            print(x, counter)
    else:
        x = 0
