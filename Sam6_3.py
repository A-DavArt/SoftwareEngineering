def count_digits(digits_str):
    digit_counts = {i: digits_str.count(str(i)) for i in range(10)}
    top_3_digits = sorted(digit_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    return dict(sorted(top_3_digits, key=lambda x: x[0]))

digits_str = "9876543210987654321098765432109876543210"
print(count_digits(digits_str))