from collections import UserString
import sys


class DivStr(UserString):
    def __init__(self, seq=""):
        super().__init__(seq)

    def __floordiv__(self, other):
        size = len(self) // other
        return iter(self[i:i + size] for i in range(0, other * size, size))

    def __mod__(self, other):
        size = len(self) % other
        return self[-size:]


exec(sys.stdin.read())