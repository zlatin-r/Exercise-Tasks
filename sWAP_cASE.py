s = input()


def swap_case(s):
    result = ''

    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                result += s[i].lower()
            else:
                result += s[i].upper()
        else:
            result += s[i]

    return result


print(swap_case(s))
