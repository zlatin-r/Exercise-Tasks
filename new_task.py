def move_zeros(array):
    for i in range(len(array)):
        if array[i] == 0:
            array.append(0)
            array.remove(array[i])
    return array


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
