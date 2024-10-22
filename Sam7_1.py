from collections import Counter
with open('input.txt', 'r', encoding='latin-1') as file:
    text = file.read()
words = text.split()
word_count = len(words)
word_frequency = Counter(words)
most_common_word, most_common_count = word_frequency.most_common(1)[0]
print(f'Количество слов: {word_count}')
print(f'Самое часто встречающееся слово: "{most_common_word}" ({most_common_count} раз)')
