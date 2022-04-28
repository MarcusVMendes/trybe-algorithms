def is_anagram(first_string, second_string):
    l1 = list(first_string.lower())
    l2 = list(second_string.lower())

    if len(l1) != len(l2):
        return False

    for letter in l1:
        if letter in l2:
            l2.remove(letter)
        else:
            return False
    return True
