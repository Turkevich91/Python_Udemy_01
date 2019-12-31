a = ["a", "b", "c"]
b = ["c", "a"]


def does_list_x_contain_y(x, y):
    if not x or not y:
        return "Empty list, process stopped"
    counter = 0

    for i in y:
        for j in x:
            if i == j:
                counter += 1
                break
    return True if len(y) == counter else False


print(does_list_x_contain_y(a, b))