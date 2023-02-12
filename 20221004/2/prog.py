def Pareto(*dots):
    return tuple(dot for dot in dots if all(dot[0] >= _[0] or dot[1] >= _[1] for _ in dots))


print(Pareto(*eval(input())))


