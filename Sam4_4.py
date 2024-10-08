def improve_grades(grades):
    new_grades = []
    for grade in grades:
        if grade == 2:
            continue
        elif grade == 3:
            new_grades.append(4)
        else:
            new_grades.append(grade)
    return new_grades

grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print("Список 1:", improve_grades(grades1))
print("Список 2:", improve_grades(grades2))
print("Список 3:", improve_grades(grades3))
