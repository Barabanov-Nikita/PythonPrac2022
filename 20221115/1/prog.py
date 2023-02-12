import sys


def objcount(cls):
    cls.counter = 0
    _tmp__init__ = cls.__init__
    def __init__(self, *args, **kwargs):
        cls.counter += 1
        _tmp__init__(self, *args, **kwargs)

    cls.__init__ = __init__
    _tmp__del__ = cls.__del__ if "__del__" in cls.__dict__ else None
    def __del__(self):
        cls.counter -= 1
        if _tmp__del__:
            _tmp__del__(self)

    cls.__del__ = __del__

    return cls

exec(sys.stdin.read())
