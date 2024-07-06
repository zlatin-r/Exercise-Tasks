from itertools import combinations_with_replacement

S, K = input().upper().split()

k = int(K)

for i in combinations_with_replacement(sorted(S), k):
    print(''.join(i), end='\n')
