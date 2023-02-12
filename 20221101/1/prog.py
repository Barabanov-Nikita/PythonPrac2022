import sys


class Omnibus:
    _attr_counts = {}

    def __setattr__(self, key, value):
        if not key.startswith("_"):
            self._attr_counts.setdefault(key, set())
            self._attr_counts[key].add(self)

    def __getattr__(self, item):
        if not item.startswith("_"):
            return len(self._attr_counts[item])

    def __delattr__(self, item):
        if self in self._attr_counts.get(item, set()):
            self._attr_counts[item] -= {self}


exec(sys.stdin.read())
