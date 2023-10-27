l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]


def list_to_num(lst1, lst2):
    num1 = ""
    num2 = ""

    for i in lst1:
        num1 += str(i)

    for i in lst2:
        num2 += str(i)

    result = str(int(num1) + int(num2))
    result = result[::-1]
    return [int(x) for x in result]


print(list_to_num(l1, l2))
