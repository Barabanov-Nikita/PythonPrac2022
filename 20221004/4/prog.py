from math import *


def Calc(s, t ,u):
    def func(x):
        y = eval(t)
        x = eval(s)
        return eval(u)
    return func


args, x = eval(input()), eval(input())
print(Calc(*args)(x))
