import re

s = input()
k = input()

matches = re.findall(k, s)

print(matches)
