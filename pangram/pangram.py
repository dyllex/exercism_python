def is_pangram(sentence):
    # Removes case sensitivity
    sentence = sentence.lower()
    # Removes repeated characters
    sentence = list(set(sentence))

    # Increments alpha_count whenever a new letter of the alphabet is used.
    alpha_count = 0
    for char in sentence:
        # Using .isalpha() so that numbers won't count
        if char.isalpha():
            alpha_count += 1
        else:
            continue

    # 26 letters in the alphabet. Returns true if all letters were used at least once.
    return alpha_count == 26
