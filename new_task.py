n, m = [int(x) for x in input().split()]

mid_row = 1
dashes = int((m - 3) / 2)


print('-' * dashes + '.|.' + '-' * dashes)

for row in range((n // 2) - 1):
    mid_row += 2
    dashes -= 3
    print('-' * dashes + '.|.' * mid_row + '-' * dashes)

print('-' * ((m - len('WELCOME')) // 2) + 'WELCOME' + '-' * ((m - len('WELCOME')) // 2))

for row in range((n // 2)):
    print('-' * dashes + '.|.' * mid_row + '-' * dashes)
    mid_row -= 2
    dashes += 3
