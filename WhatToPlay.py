import random

print("Insert list of games:  \nLeave blank if you want to finish")
games = []

x = 0
count = 0


def addLine():
    print("#", count+1)
    new = input()
    return new


while count == 0 or x != "":
    x = addLine()
    games.append(x)
    count += 1


print("Random game is:", games[random.randint(0, len(games)-2)])

