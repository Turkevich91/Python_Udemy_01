from comparator import does_list_x_contain_y as conflict
left = ['goat', 'cabbage','wolf']
right = []
isLeftSide = True
exceptions = [["wolf", "goat"], ["goat", "cabbage"]]
# exception1 = ["wolf", "goat"]
# exception2 = ["goat", "cabbage"]


def take_to_board_from(side):
    for i in range(len(side)):
        t = side.pop(i)
        if not side:
            return t
        elif conflict(side, exceptions[0]) or conflict(side, exceptions[1]):
            side.insert(i, t)
        else:
            return t


print("left side:", left, "\nStart:\n")


while len(right) < 3:
    if isLeftSide:  # move from left to right
        right.append(take_to_board_from(left))
        print(left, " => ", right)
    elif conflict(right, exceptions[0]) or conflict(right, exceptions[1]):
        left.append(take_to_board_from(right))
        print(left, " <= ", right)
    else:
        print(" <== return empty ==<< ")
    isLeftSide = not isLeftSide

print("\nFinish")
