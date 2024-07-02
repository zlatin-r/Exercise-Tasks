import re

S = input().strip()
k = input().strip()

# Find all occurrences of the substring k in S
matches = re.finditer(r'(?={})'.format(re.escape(k)), S)

# Print the start and end indices of each match
found = False
for match in matches:
    start_index = match.start()
    end_index = start_index + len(k) - 1
    print(f"({start_index}, {end_index})")
    found = True

if not found:
    print("(-1, -1)")
