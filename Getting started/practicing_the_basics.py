def is_question(sentence):
    question_words = ('What', 'Where', 'When', 'How', 'Why', 'Do')
    return sentence.startswith(question_words)

def sentence_maker(sentence):
    capitalized_sentence = sentence.capitalize()

    if capitalized_sentence.endswith(('?','.')):
        return capitalized_sentence
    else:
        if is_question(capitalized_sentence):
            return capitalized_sentence + '?'
        else:
            return capitalized_sentence + '.'
    
sentences = []
while True:
    new_sentence = input('Say something: ')
    if new_sentence == '\end':
        print(' '.join(sentences))
        break
    else:
        sentences.append(sentence_maker(new_sentence))
        continue
