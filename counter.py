import random

x = 0
counter = 0
value = 0


def drop():
    return random.randint(1, 6)


while x <= 2:
    counter += 1
    a, b = drop(), drop()
    value += a + b
    if a == b:
        x += 1
        if x >= 1:
            print(x, counter, value, value/counter/2)
    else:
        x = 0
