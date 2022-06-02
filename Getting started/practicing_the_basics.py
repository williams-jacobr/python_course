sentences = []

def is_question(word):
    question_words = ['what', 'where', 'when', 'how', 'why', 'do']
    if word.lower() in question_words:
        return True

def add_sentence(sentence):
    word_list = sentence.split()
    if is_question(word_list[0]):
        word_list.append('?')
    else:
        word_list.append('.')
    word_list[0] = word_list[0].title()

    correct_sentence = ' '.join([str(item) for item in word_list])

    print(correct_sentence)

    sentences.append(correct_sentence)

while True:
    new_sentence = input('Say something: ')
    if new_sentence == '\end':
        print(' '.join([str(item) for item in sentences]))
        break
    else:
        add_sentence(new_sentence)
        continue
