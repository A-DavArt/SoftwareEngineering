def text_statistics(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    letter_count = 0
    word_count = 0
    line_count = len(lines)

    for line in lines:
        letter_count += sum(c.isalpha() for c in line)
        word_count += len(line.split())

    print(f'{letter_count} letters')
    print(f'{word_count} words')
    print(f'{line_count} lines')


text_statistics('input.txt')