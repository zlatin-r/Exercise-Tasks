def solve(s):
    words = s.split(' ')
    result = []

    for word in words:
        result.append(word.capitalize())

    return " ".join(result)


print(solve('hello world lol 1a'))
