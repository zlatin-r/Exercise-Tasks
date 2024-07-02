import re

S = input()
k = input()

matches = re.finditer(f'(?={k})', S)

found = False

for match in matches:
    start_index = match.start()
    end_index = start_index + len(k) - 1
    print(f"({start_index}, {end_index})")
    found = True

if not found:
    print("(-1, -1)")
