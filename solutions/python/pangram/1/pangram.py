def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence_lowered = sentence.lower()
    for letter in alphabet:
        if letter not in sentence_lowered:
            return False
    return True