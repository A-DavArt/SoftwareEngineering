from tttt import triangle_area
def main():
    print("Вычисление площади треугольника")
    a = float(input("Введите длину первой стороны: "))
    b = float(input("Введите длину второй стороны: "))
    c = float(input("Введите длину третьей стороны: "))
    area = triangle_area(a, b, c)
    print(f"Площадь треугольника: {area:.2f} кв. единиц")
if __name__ == "__main__":
    main()