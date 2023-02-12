from math import sqrt
import sys


class Triangle:
    def __init__(self, p0, p1, p2):
        self.p0, self.p1, self.p2 = p0, p1, p2
        self.a = p0[0] - p1[0], p0[1] - p1[1]
        self.b = p1[0] - p2[0], p1[1] - p2[1]
        self.c = p2[0] - p0[0], p2[1] - p0[1]

    def __abs__(self):
        def l(p):
            return sqrt(p[0] * p[0] + p[1] * p[1])

        a, b, c = self.a, self.b, self.c
        s = 0.5 * abs(a[0] * c[1] - c[0] * a[1]) \
            if max(l(a), l(b), l(c)) <= min(l(a) + l(b), l(b) + l(c), l(c) + l(a)) \
            else 0
        return s

    def __bool__(self):
        return bool(abs(self))

    def __lt__(self, other):
        return abs(self) < abs(other)

    def muls(self, item):
        x, y = item
        x0, y0 = self.p0
        x1, y1 = self.p1
        x2, y2 = self.p2
        a = (x0 - x) * (y1 - y0) - (x1 - x0) * (y0 - y)
        b = (x1 - x) * (y2 - y1) - (x2 - x1) * (y1 - y)
        c = (x2 - x) * (y0 - y2) - (x0 - x2) * (y2 - y)
        return a, b, c

    def __contains__(self, item):
        if type(item) is tuple:
            a, b, c = self.muls(item)
            return a * b >= 0 and b * c >= 0 and a * c >= 0
        elif item.__class__ == Triangle:
            return item.p0 in self and item.p1 in self and item.p2 in self if item else True

    def __and__(self, other):
        if not (self and other):
            return False
        for dot in other.p0, other.p1, other.p2:
            a, b, c = self.muls(dot)
            if a * b > 0 and b * c > 0:
                return True
        return False
        # def trianglein(other, self):
        #     return not (other.p0 in self and other.p1 in self and other.p2 in self) \
        #        and (other.p0 in self or other.p1 in self or other.p2 in self)

        # return bool(self) and bool(other) and (trianglein(self, other) or trianglein(other, self))

exec(sys.stdin.read())
