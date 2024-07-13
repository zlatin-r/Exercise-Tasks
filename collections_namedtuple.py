from collections import namedtuple

total_students = int(input())
Student = namedtuple("Student", input().split())
sum_marks = 0

for i in range(total_students):
    data = input().split()

    s = Student(data[0], data[1], data[2], data[3])

    sum_marks += int(s.MARKS)

print(f"{sum_marks / total_students:.2f}")

# students_num, total, student = int(input()), 0, namedtuple('student', ",".join(input().split()))
# print(sum(int(student(*[a for a in input().split()]).MARKS) for a in range(students_num)) / students_num)

# input:

# 5
# CLASS      NAME       MARKS      ID
# 4          Iain       96         1
# 2          Jeremy     77         2
# 5          Derek      94         3
# 4          Ryan       52         4
# 3          Leslie     85         5

# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6
