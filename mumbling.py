def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


# def accum(s):
#     str = ""
#     for i in range(0, len(s)):
#         str += s[i].upper()
#         str += s[i].lower() * i
#         if i != len(s) - 1:
#             str += "-"
#     return str


print(accum("abcd"))
