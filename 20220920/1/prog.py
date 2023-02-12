x = int(input())
s = ""
if not x % 25:
    if not x % 2:
        s += "A + B - "
    else:
        s += "A - B + "
else:
    s += "A - B - "
if not x % 8:
    s += "C +"
else:
    s += "C -"

print(s)
