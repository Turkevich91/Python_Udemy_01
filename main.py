from comparator import does_list_x_contain_y as compare
# w = wolf, g = goat, c = cabbage
side1 = ['w', 'g', 'c']
side2 = []
isLeftSide = True
# b = None
exception1 = ["w", "g"]
exception2 = ["g", "c"]


def switcher():
    global isLeftSide
    isLeftSide = not isLeftSide


def indexer(side):
    for i in side:
        t = side.pop(i)
        if compare(side, exception1) or compare(side, exception2):
            side.insert(i, t)
        else:
            return i


while len(side2) != 3:
    if isLeftSide:  # move from left to right
        side2.append(side1.pop(indexer(side1)))
    elif compare(side2, exception1) or compare(side2, exception1):
        side1.append(side2.pop(indexer(side2)))
    print(side1, " => ", side2)
    switcher()

print("\n\nFinish")
    # remove wolf from side 1 and move it to side 2

    # side2.append(side1.pop(0))  переместить первый элемент первого списка в конец второго списка
    # isLeftSide = not isLeftSide
    # list.append(Var)
    # list.pop(0) - удалить и вернуть последний элемент списка, или его индекс.
