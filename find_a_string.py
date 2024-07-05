string = input()
substring = input()


def count_substring(string, substring):
    counter = 0
    for i in range(len(string)):
        if string[i:i + len(substring)] == substring:
            counter += 1

    return counter


print(count_substring(string, substring))
