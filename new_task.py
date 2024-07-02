if __name__ == '__main__':
    N = int(input())

    arr = []

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            idx = int(command[1])
            value = int(command[2])
            arr.insert(idx, value)

        elif command[0] == "remove":
            value = int(command[1])
            arr.remove(value)

        elif command[0] == "append":
            value = int(command[1])
            arr.append(value)

        elif command[0] == "print":
            print(arr)

        elif command[0] == "sort":
            arr.sort()

        elif command[0] == "pop":
            arr.pop()

        elif command[0] == "reverse":
            arr.reverse()
