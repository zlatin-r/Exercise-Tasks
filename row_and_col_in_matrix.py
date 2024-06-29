data = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]


def Solution(matrix: list[list[int]]):
    n = len(matrix)

    for row in matrix:
        if len(set(row)) != n:
            return False

    for col in range(n):
        col_set = set(matrix[row][col] for row in range(n))
        if len(col_set) != n:
            return False

    return True


print(Solution(data))
