import random

x = 0
counter = 0
value = 0
maxRange = 6
coincidences = 2   #2 default


def drop():
    return random.randint(1, maxRange)


while x <= coincidences:
    counter += 1
    a, b = drop(), drop()
    value += a + b
    if a == b:
        x += 1
        if x >= 2:
            print(x, counter, value, value/counter/2)
    else:
        x = 0
