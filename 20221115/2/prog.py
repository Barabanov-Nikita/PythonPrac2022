import sys


class Num:
    _val = 0
    def __get__(self, instance, owner):
        if not hasattr(instance, "_val"):
            instance._val = 0
        return instance._val

    def __set__(self, instance, value):
        if hasattr(value, "real"):
            instance._val = value.real
        elif hasattr(value, "__len__"):
            instance._val = len(value)

    def __delete__(self, instance):
        del instance._val


exec(sys.stdin.read())
