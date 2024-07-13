from collections import Counter

number_of_shoes = int(input())
total_shoes_in_store = Counter(map(int, input().split()))
number_of_customers = int(input())
total_win = 0

for customer in range(number_of_customers):
    desired_size, price = map(int, input().split())

    if desired_size in total_shoes_in_store.keys():
        if total_shoes_in_store[desired_size] > 0:
            total_shoes_in_store[desired_size] -= 1
            total_win += price

print(total_win)
