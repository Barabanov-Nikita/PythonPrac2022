def binsearch(elem, a):
    if not a:
        return False
    idx = (len(a) - 1) // 2
    check = a[idx]
    if check == elem:
        return True
    elif check > elem:
        return binsearch(elem, a[:idx])
    else:
        return binsearch(elem, a[idx + 1:])


print(binsearch(*eval(input())))
