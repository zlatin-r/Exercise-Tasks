group_size = int(input())
room_numbers = list(map(int, input().split()))
set_nums = set(room_numbers)

for i in set_nums:
    room_numbers.remove(i)
    if i not in room_numbers:
        print(i)
        break
