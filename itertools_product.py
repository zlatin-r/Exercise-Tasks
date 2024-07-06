from itertools import product

a = map(int, input().split())
b = map(int, input().split())

c = product(a, b)

print(*list(c))

# for i in range(len(a)):
#     for j in range(len(b)):
#         print((int(a[i]),int(b[j])), end=' ')
