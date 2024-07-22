num_el_a = int(input())
a = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command, set_len = input().split()
    b = set(map(int, input().split()))

    if command == "update":
        a.update(b)
    elif command == "intersection_update":
        a.intersection_update(b)
    elif command == "difference_update":
        a.difference_update(b)
    elif command == "symmetric_difference_update":
        a.symmetric_difference_update(b)

print(sum(a))

