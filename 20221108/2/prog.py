from math import sqrt


class InvalidInput(Exception):
    pass


class BadTriangle(Exception):
    pass


def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except Exception:
        raise InvalidInput

    def l(x, y):
        return sqrt(x * x + y * y)

    a, b, c = l(x1 - x2, y1 - y2), l(x2 - x3, y2 - y3), l(x3 - x1, y3 - y1)
    if max(a, b, c) >= min(a + b, b + c, c + a):
        raise BadTriangle
    return 1/2 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

while True:
    try:
        s = triangleSquare(input())
    except InvalidInput:
        print("Invalid Input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print("%.2f" % s)
        break

