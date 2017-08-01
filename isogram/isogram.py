# Hacked together. Would appreciate pointers on how to clean this up. 

# def is_isogram(word):
#     l_word = word.lower()
#     new = l_word.replace('-', '')
#     new2 = new.replace(' ', '')
#     return len(new2) == len(set(new2))


def is_isogram(word):
    word = word.lower()
    for letter in word:
        if letter.isalpha() and word.count(letter) > 1:
            return False

    return True

