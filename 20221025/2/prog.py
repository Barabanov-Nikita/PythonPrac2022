from itertools import tee, islice
import sys

def slide(seq, n):
    loopseq, seq = tee(seq)
    for idx, _ in enumerate(loopseq):
        tmp, seq = tee(seq, 2)
        yield from islice(tmp, idx, idx + n)


exec(sys.stdin.read())
