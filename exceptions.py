n = int(input())

for _ in range(n):

    a, b = input().split()

    try:
        print(int(a) // int(b))
    except ZeroDivisionError as z:
        print("Error Code:", z)
    except ValueError as v:
        print("Error Code:", v)

