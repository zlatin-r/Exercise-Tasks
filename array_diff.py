def array_diff(a, b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)
    return result


# def array_diff(a, b):
#     return [x for x in a if x not in b]


print(array_diff([1, 2, 3], [1, 2]))
