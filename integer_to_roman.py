# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

s = str(input())
s = int(s)

result = ""

if 1000 <= s < 4000:
    result += (s // 1000) * "M"
    s = s % 1000
if 900 <= s < 1000:
    result += (s // 900) * "CM"
    s = s % 900
if 500 <= s < 900:
    result += (s // 100) * "D"
    s = s % 100
if 400 <= s < 500:
    result += (s // 400) * "CD"
    s = s % 400
if 100 <= s < 400:
    result += (s // 100) * "C"
    s = s % 100
if 90 <= s < 100:
    result += (s // 90) * "XC"
    s = s % 90
if 50 <= s < 90:
    result += (s // 50) * "L"
    s = s % 50
if 40 <= s < 50:
    result += (s // 40) * "XL"
    s = s % 40
if 10 <= s < 40:
    result += (s // 10) * "X"
    s = s % 10
if s == 9:
    result += (s // 9) * "IX"
    s = s % 9
if 5 <= s < 9:
    result += "V" + (s % 5) * "I"
if s == 4:
    result += (s // 4) * "IV"
    s = s % 4
if 1 <= s < 4:
    result += s * "I"

print(result)
