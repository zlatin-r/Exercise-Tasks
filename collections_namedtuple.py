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
