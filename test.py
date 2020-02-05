import random
import math


def calc():
    a = 15
    x = random.uniform(0, 15)
    y = (a*a-x*x)**.5
    return x, y, a


for i in range(1, 1001):
    x,y,a = calc()
    koef = a/(x+y)
    print(i,": ", x,y,a, koef)