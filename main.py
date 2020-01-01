from comparator import does_list_x_contain_y as compare
# w = wolf, g = goat, c = cabbage
left = ['wolf', 'goat', 'cabbage']
right = []
isLeftSide = True
exception1 = ["wolf", "goat"]
exception2 = ["goat", "cabbage"]


def indexer(side):
    for i in range(len(side)):
        t = side.pop(i)
        if compare(side, exception1) or compare(side, exception2):
            side.insert(i, t)
        else:
            return t


print("left side:", left, "\nStart:\n")


while len(right) != 3:
    if isLeftSide:  # move from left to right
        right.append(indexer(left))
        print(left, " => ", right)
    elif compare(right, exception1) or compare(right, exception1):
        left.append(indexer(right))
        print(left, " <= ", right)
    else:
        print(left, " <== move empty ==<< ", right)
    isLeftSide = not isLeftSide

print("\nFinish")
