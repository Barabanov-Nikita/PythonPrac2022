a = eval(input())
a = list(a) if type(a) == tuple else [a, ]

for i in range(len(a)):
    for j in range(i):
        if (a[i] * a[i]) % 100 < (a[j] * a[j]) % 100:
            a[i], a[j] = a[j], a[i]

print(a)
