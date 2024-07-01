n = int(input())
arr = list(map(int, input().split()))

set_arr = set(arr)
max_el = max(set_arr)
set_arr.remove(max_el)

print(max(set_arr))
