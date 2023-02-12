from math import *
s = input().split(maxsplit=4)
w, h, a, b, y = int(s[0]), int(s[1]), float(s[2]), float(s[3]), s[4]
step = (a - b) / w
x, vals = a, []
for _ in range(w):
    vals.append(eval(y))
    x += step
ymax, ymin = max(vals), min(vals)
ans = [[" "] * w for _ in range(h)]
ans_vals = [h - 1 - round((val - ymin) * (h - 1)/(ymax - ymin)) for val in vals]
prev = ans_vals[0]
for i in range(w):
    for _ in range(prev, ans_vals[i], 1 if ans_vals[i] > prev else - 1):
        ans[_][i] = "*"
    prev = ans_vals[i]
print("\n".join(["".join(a) for a in ans]))