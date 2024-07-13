from collections import OrderedDict

data = OrderedDict()
number_items = int(input())

for i in range(number_items):
    item_and_price = input().split()

    item = " ".join(item_and_price[:-1])
    price = int(item_and_price[-1])

    if item not in data:
        data[item] = price
    else:
        data[item] += price

[print(i, p) for i, p in data.items()]
