data = []

for _ in range(int(input())):
    name = input()
    score = float(input())

    name_grade = []

    name_grade.append(name)
    name_grade.append(score)

    data.append(name_grade)

sorted_data = sorted(data, key=lambda x: x[1])

min_grade = min(grade[1] for grade in sorted_data)

removed_min_grades = [sublist for sublist in sorted_data if sublist[1] != min_grade]

min_grade = min(grade[1] for grade in removed_min_grades)

filtered_list = [sublist for sublist in removed_min_grades if sublist[1] == min_grade]

result = '\n'.join(name[0] for name in sorted(filtered_list))

print(result)
