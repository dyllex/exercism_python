def is_isogram(word):
    
    word = [char.lower() for char in word if char.isalpha()]
    return len(word) == len(set(word))
