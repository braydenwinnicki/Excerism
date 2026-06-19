def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    fixed = sentence.strip().lower()

    for letter in alphabet:
        if letter not in fixed:
            return False
    return True
        
