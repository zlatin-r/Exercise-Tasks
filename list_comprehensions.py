# Reading input values
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# List comprehension to generate the coordinates
result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

# Printing the resulting list
print(result)

