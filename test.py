from comparator import does_list_x_contain_y as compare

side1 = ['w', 'g', 'c']
side2 = []
isLeftSide = True
exception1 = ["w", "g"]
exception2 = ["g", "c"]
t = 0


def indexer(side):
    for i in range(len(side)):
        return side.pop(i)


print(indexer(side1))


print(side1)
print(t)
