def print_formatted(number):
    # your code goes here

    width = len(bin(number)) - 2

    for x in range(1, number + 1):
        print(str(x).rjust(width, " "),
              oct(x)[2:].rjust(width, " "),
              hex(x)[2:].rjust(width, " ").upper(),
              bin(x)[2:].rjust(width, " "))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
