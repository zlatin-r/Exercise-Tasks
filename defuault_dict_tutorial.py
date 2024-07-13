from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(n):
    d[input()].append(i + 1)

for j in range(m):
    B = input()
    key = d.keys()

    if B in key:
        print(*d[B])
    else:
        print(-1)
