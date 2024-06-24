def merge_the_tools(string, k):
    for s in range(0, len(string), k):
        substring = (string[s:s + k])

        seen = set()
        result = []

        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)

        print(''.join(result))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
