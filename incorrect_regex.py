from re import compile

n = int(input())

for _ in range(n):
    try:
        r = compile(input())
        print(True)
    except:
        print(False)
