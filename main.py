# w = wolf, g = goat, c = cabbage
side1 = ['w', 'g', 'c']
side2 = []
isLeftSide = True
b = None
exception1 = ("w", "g")
exception2 = ("g", "c")


def switcher():
    global isLeftSide
    isLeftSide = not isLeftSide


def indexer(side):
    for i in side:
        side.pop(i)
        if exception1 or exception2 in side:




# def checking ():
while len(side2) != 3:
    if isLeftSide:  # move from left to right
        # b = side1.pop(0)
        switcher()
    #         if exception1[0] and exception1[1] in side1:
    #             te
    #         elif exception2[0] and exception2[1] in side1:
    #             b =
    #     elif
    #         print("Right side: \n")
    else:  # move from right to left
        side2.append(b)
        switcher()

    # remove wolf from side 1 and move it to side 2

    # side2.append(side1.pop(0))  переместить первый элемент первого списка в конец второго списка
    # isLeftSide = not isLeftSide
    # list.append(Var)
    # list.pop(0) - удалить и вернуть последний элемент списка, или его индекс.
