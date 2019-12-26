# w = wolf, g = goat, c = cabbage
side1 = ['w', 'g', 'c']
side2 = []
isLeftSide = True
b = None
exception1 = ("w", "g")
exception2 = ("g", "c")

# side2.append('w')
# side2.append('g')
# print(side2)
# side2.pop(side2.index("w"))
#
# print(side2)
# side2.append('w')
# print(side2)


def switcher():
    global isLeftSide
    isLeftSide = not isLeftSide


#def checking ():
while len(side1) > 0:
    if isLeftSide:   #move from left to right

        switcher()
#         if exception1[0] and exception1[1] in side1:
#             te
#         elif exception2[0] and exception2[1] in side1:
#             b =
#     elif
#         print("Right side: \n")
    else: #move from right to left

        switcher()





    # remove wolf from side 1 and move it to side 2

    # isLeftSide = not isLeftSide
    # list.append(Var)
    # list.pop(0) - удалить и вернуть последний элемент списка, или его индекс.
