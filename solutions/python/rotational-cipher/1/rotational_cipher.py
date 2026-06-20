
def rotate(text, key):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    new_text = []
    
    for letter in text: 
        if not letter.isalpha():
            new_text.append(letter)
        elif letter.isupper():
            index = alphabet.index(letter.lower())
            new_char = alphabet[(index + key) % 26]
            new_text.append(new_char.upper())
        elif letter.islower():
            index = alphabet.index(letter)
            new_char = alphabet[(index + key) % 26]
            new_text.append(new_char)

    return "".join(new_text)
        
        
            
            
