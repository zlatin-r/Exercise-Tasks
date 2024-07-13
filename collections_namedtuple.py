from collections import namedtuple

total_students = int(input())
fields = input().split()
student = namedtuple('student', 'id, marks, name, class')
data = []
sum_marks = 0

for i in range(total_students):
    s = student(input().split())
    sum_marks += s.marks
