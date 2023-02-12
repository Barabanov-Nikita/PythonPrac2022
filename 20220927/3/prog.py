a = [list(eval(input())), ]
n = len(a[0])
a, b = a + [list(eval(input())) for _ in range(n - 1)], [list(eval(input())) for _ in range(n)]
c = [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
for row in c:
    print(*row, sep=",")
