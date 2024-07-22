m = int(input())
arr_m = set(map(int, input().split()))

n = int(input())
arr_n = set(map(int, input().split()))

res1 = list(arr_m.difference(arr_n))
res2 = list(arr_n.difference(arr_m))

res = res1 + res2

print("\n".join(map(str, sorted(res))))
