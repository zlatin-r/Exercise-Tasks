from collections import OrderedDict

data = OrderedDict()
n = int(input())

for _ in range(n):
    word = input()

    if word not in data:
        data[word] = 1
    else:
        data[word] += 1

values = [v for k, v in data.items()]

print(len(data))
print(*values)
