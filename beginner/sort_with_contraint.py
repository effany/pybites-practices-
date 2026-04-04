def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    digit_array = []
    word_collection = []
    for word in words:
        if word[0].isdigit():
            digit_array.append(word)
        else:
            word_collection.append(word)
    print(sorted(word_collection, key=str.lower) +  sorted(digit_array))
    return sorted(word_collection, key=str.lower) +  sorted(digit_array)
    


