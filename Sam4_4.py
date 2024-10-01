def calculate_average(*args):
    if not args:
        return 0.0
    total = sum(args)
    count = len(args)
    return total / count
if __name__ == "__main__":
    result = calculate_average(5, 10, 15, 20, 25)
    print(f"Среднее арифметическое: {result:.2f}")
