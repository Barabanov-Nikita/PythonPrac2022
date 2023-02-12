m, n = eval(input())
print([i for i in range(m, n) if all(i % _ for _ in range(2, int(i**0.5) + 1)) and i != 1])
