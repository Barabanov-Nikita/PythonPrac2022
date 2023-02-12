import string
import sys
from collections import Counter
w = int(input())
text = "".join(sys.stdin.readlines())
clean = string.punctuation + string.digits
for c in clean:
    text = text.replace(c, " ")

text = text.lower()
d = {}
for word in text.split():
    if len(word) == w:
        d.setdefault(word, 0)
        d[word] += 1

top = sorted(d.items(), key=lambda x: x[1], reverse=True)
if top:
    top_count = top[0][1]
    i = 0
    while i < len(top) and ((cur_count := top[i][1]) == top_count):
        i += 1
    print(*sorted(_[0] for _ in top[:i]))

