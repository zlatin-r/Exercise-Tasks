line = input()


def split_and_join(line):
    arr_line = line.split(' ')

    return '-'.join(arr_line).strip('-')


print(split_and_join(line))
