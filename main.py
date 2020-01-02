from comparator import does_list_x_contain_y as conflict
left = ['goat', 'cabbage', 'wolf']
right = []
isLeftSide = True
exception1 = ["wolf", "goat"]
exception2 = ["goat", "cabbage"]


def take_to_board_from(side):
    for i in range(len(side)):
        t = side.pop(i)
        if not side:
            return t
        elif conflict(side, exception1) or conflict(side, exception2):
            side.insert(i, t)
        else:
            return t


print("left side:", left, "\nStart:\n")


while len(right) < 3:
    if isLeftSide:  # move from left to right
        right.append(take_to_board_from(left))
        print(left, " => ", right)
    elif conflict(right, exception1) or conflict(right, exception2):
        left.append(take_to_board_from(right))
        print(left, " <= ", right)
    else:
        print(left, " <== move empty ==<< ", right)
    isLeftSide = not isLeftSide

print("\nFinish")
