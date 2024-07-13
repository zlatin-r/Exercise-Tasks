from collections import deque

d = deque()
N = int(input())

for i in range(N):
    in_put = input().split()

    if len(in_put) == 2:
        if in_put[0] == "append":
            d.append(int(in_put[1]))

        elif in_put[0] == "appendleft":
            d.appendleft(int(in_put[1]))

    elif in_put[0] == "pop":
        d.pop()

    elif in_put[0] == "popleft":
        d.popleft()

for i in range(len(d)):
    print(d[i], end=" ")

