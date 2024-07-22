english_subs = int(input())
en_students = set(map(int, input().split()))
french_subs = int(input())
fr_students = set(map(int, input().split()))

print(len(en_students.symmetric_difference(fr_students)))

