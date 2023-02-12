from inspect import get_annotations
import types
import sys

class check(type):
    def __init__(cls, name, parents, ns, **kwds):
        def check_annotations(self):
            for name, an_typ in get_annotations(self.__class__).items():
                try:
                    attr = getattr(self, name)
                except AttributeError:
                    return False
                if not callable(attr):
                    typ = type(attr)
                    if type(an_typ) == types.GenericAlias:
                        an_typ = an_typ.__origin__
                    if typ is not an_typ and not issubclass(typ, an_typ):
                        return False
            return True
        setattr(cls, check_annotations.__name__, check_annotations)
        super().__init__(name, parents, ns)


exec(sys.stdin.read())