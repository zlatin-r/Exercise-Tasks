def unique_in_order(iterable):
    result = []
    prev = None

    for item in iterable:
        if item != prev:
            result.append(item)
            prev = item

    return result


# def unique_in_order(iterable):
#     res = []
#     for item in iterable:
#         if len(res) == 0 or item != res[-1]:
#             res.append(item)
#     return res


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order((1, 2, 2, 3, 3)))
