s = input().lower()
u_pairs = set()
count = 0
for i in range(2, len(s) + 1):
    pair = s[i-2: i]
    if pair.isalpha() and pair not in u_pairs:
        u_pairs.add(pair)
        count += 1

print(count)