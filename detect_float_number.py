import re

pattern = r"^[-+]?[0-9]*\.[0-9]+$"

n = int(input())

for i in range(n):
    try:
        num_str = input()
        if not re.match(pattern, num_str):
            print("False")
        else:
            print("True")
    except ValueError:
        print("False")
