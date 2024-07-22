n = int(input())

for _ in range(n):
    el_a = int(input())
    a = set(map(int, input().split()))
    el_b = int(input())
    b = set(map(int, input().split()))

    print(a.issubset(b))
