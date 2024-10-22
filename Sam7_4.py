def load_prohibited_words(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split()

def filter_sentence(sentence, prohibited_words):
    for word in prohibited_words:
        sentence = sentence.replace(word, '*' * len(word))
        sentence = sentence.replace(word.capitalize(), '*' * len(word))
    return sentence

prohibited_words = load_prohibited_words('input.txt')
sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is… PYTHON is awesome!!!!"
filtered_sentence = filter_sentence(sentence.lower(), prohibited_words)

print(filtered_sentence)