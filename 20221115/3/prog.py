import string
import sys

class Alpha:
    __slots__ = list(string.ascii_lowercase)

    def __init__(self, **kwargs):
        for c in kwargs:
            self.__setattr__(c, kwargs[c])

    def __str__(self):
        return ", ".join(c + ": " + str(self.__getattribute__(c)) for c in self.__slots__ if hasattr(self, c))


class AlphaQ:
    def __init__(self, **kwargs):
        for c in kwargs:
            if c in string.ascii_lowercase:
                self.__setattr__(c, kwargs[c])
            else:
                raise AttributeError

    def __setattr__(self, key, value):
        if key in string.ascii_lowercase:
            self.__dict__[key] = value
        else:
            raise AttributeError

    def __str__(self):
        return ", ".join(c + ": " + str(self.__getattribute__(c)) for c in string.ascii_lowercase if hasattr(self, c))


exec(sys.stdin.read())
