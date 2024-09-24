sentence = input("Введите предложение на английском языке: ")

print("Длина предложения:", len(sentence))

lowercase_sentence = sentence.lower()
print("Предложение в нижнем регистре:", lowercase_sentence)

vowels = "aeiou"
vowel_count = sum(sentence.lower().count(v) for v in vowels)
print("Количество гласных:", vowel_count)

replaced_sentence = sentence.replace("ugly", "beauty")
print("Предложение с заменой 'ugly' на 'beauty':", replaced_sentence)

if sentence.startswith("The") and sentence.endswith("end"):
    print("Предложение начинается с 'The' и заканчивается на 'end'.")
else:
    print("Предложение не начинается с 'The' или не заканчивается на 'end'.")
