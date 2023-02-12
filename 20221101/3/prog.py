from math import log
import sys

class Grange:
    def __init__(self, b0, q, bn):
        self.b0, self.q, self.bn = b0, q, bn

    def __len__(self):
        if (n := int((self.bn / self.b0))) == 1:
            return 0
        return int(log(n - 1, self.q)) + 1

    def __bool__(self):
        return bool(len(self))

    def __getitem__(self, i):
        if type(i) == int:
            return self.b0 * self.q**i
        elif type(i) == slice:
            return Grange(i.start, self.q**i.step if i.step else self.q, i.stop)

    def __iter__(self):
        if len(self):
            self.prev = self.b0
            yield self.prev
            for i in range(1, len(self)):
                self.prev *= self.q
                yield self.prev

    def __str__(self):
        return f"grange({self.b0}, {self.q}, {self.bn})"

    __repr__ = __str__


exec(sys.stdin.read())
