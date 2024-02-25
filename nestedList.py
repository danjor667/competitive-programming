if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
students.sort(key=lambda x: x[1])
lowest = students[0][1]
for student in students:
    if student[1] != lowest:
        second_lowest = student[1]
        break
    else:
        second_lowest = lowest
res = []
for student in students:
    if student[1] == second_lowest:
        res.append(student[0])
res.sort(key=lambda x: x[0])
for name in res:
    print(name)
