def subtracter(x, y):
    if type(x) == list and type(y) == list:
        return [_ for _ in x if _ in set(x).difference(set(y))]
    elif type(x) == tuple and type(y) == tuple:
        return tuple(_ for _ in x if _ in set(x).difference(set(y)))
    else:
        return x - y

print(subtracter(*eval(input())))