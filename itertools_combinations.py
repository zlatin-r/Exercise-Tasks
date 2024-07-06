from itertools import combinations

S, K = input().upper().split()

k = int(K)

result = []
for i in range(1, k + 1):
    result.extend(combinations(sorted(S), i))

for j in result:
    print(''.join(j))
