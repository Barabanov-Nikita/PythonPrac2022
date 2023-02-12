n = int(input())
x = n
while x <= n + 2:
    y = n
    while y <= n + 2:
        mul = x * y
        res = 0
        while mul > 0:
            res += mul % 10
            mul //= 10
        print(x, "*", y, "=", ":=)" if res == 6 else x * y, sep=" ", end=" ")
        y += 1
    x += 1
    print()

