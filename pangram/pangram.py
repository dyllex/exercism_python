def is_pangram(sentence):
    
    # Was able to refactor using list comprehension. 
    # Creates a set of alpha characters from lowercase input sentence.
    # Then checks if length of set is equal to letters in alphabet (26)
    return len({x for x in sentence.lower() if x.isalpha()}) == 26
