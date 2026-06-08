"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""

    return "un" + word 
    
def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words."""

    return (" :: " + vocab_words[0]).join(vocab_words)
    
   
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind."""

    no_suffix = word[:-4]

    if no_suffix[-1] == "i":
        return no_suffix[:-1] + "y"
    return no_suffix

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""

    new_word = sentence.split()[index]

    if "." in new_word:
        return new_word[:-1] + "en"
    return new_word + "en"    