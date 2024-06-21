def high_and_low(numbers):
    numbers = ' '.join(str(n) for n in [max(int(x) for x in numbers.split()), min(int(y) for y in numbers.split())])
    return numbers


# def high_and_low(numbers):
#   numbers = [int(c) for c in numbers.split(' ')]
#   return f"{max(numbers)} {min(numbers)}"


print(high_and_low("1 2 3 4 5"))  # return "5 1"
print(high_and_low("1 2 -3 4 5"))  # return "5 -3"
print(high_and_low("1 9 3 4 -5"))  # return "9 -5"
