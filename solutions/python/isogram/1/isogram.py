def is_isogram(string):
    string = string.strip().lower()
    for letter in string:
        if letter.isalpha():
            if letter in string:
                string = string.replace(letter, "", 1)
            if letter in string:
                return False
    return True
