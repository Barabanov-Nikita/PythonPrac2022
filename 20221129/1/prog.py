from functools import wraps
import sys


def dec(fun):
    @wraps(fun)
    def nfun(self, *args, **kwargs):
        print(nfun.__name__, ": ", args, ", ", kwargs, sep="")
        return fun(self, *args, **kwargs)
    return nfun

class dump(type):
    def __init__(cls, name, parents, ns, **kwds):
        for n, val in ns.items():
            if callable(val):
                setattr(cls, n, dec(val))
        super().__init__(name, parents, ns)


exec(sys.stdin.read())
