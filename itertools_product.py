from itertools import product

a = map(int, input().split())
b = map(int, input().split())

c = product(a, b)

print(*list(c))
