import sys
txt = sys.stdin.buffer.read()
n, first = txt[0], txt[0:1]
txt = txt[1:]
l = len(txt)
parts = []
for i in range(n):
    part = txt[round(i*l/n):round((i+1)*l/n)]
    if part:
        parts.append(part)
sys.stdout.buffer.write(first + b"".join(sorted(parts)))
