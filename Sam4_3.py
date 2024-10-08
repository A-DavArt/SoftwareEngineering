import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

max_one, min_one = max(one), min(one)
max_two, min_two = max(two), min(two)
max_three, min_three = max(three), min(three)

max_triangle_area = triangle_area(max_one, max_two, max_three)
min_triangle_area = triangle_area(min_one, min_two, min_three)

print(f"Площадь треугольника из максимальных сторон: {max_triangle_area:.2f}")
print(f"Площадь треугольника из минимальных сторон: {min_triangle_area:.2f}")