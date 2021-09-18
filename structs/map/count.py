def count_words(sentence):
    counts = {}

    words = sentence.split(" ")
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    return counts

def count_letters(sentence):
    counts = {}

    for letter in sentence:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
    
    return counts

def count_duplicates(word):
    duplicates = {}
    counts = {}

    for letter in word:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
    
    for letter in counts:
        if counts[letter] > 1:
            duplicates[letter] = counts[letter]
    
    return duplicates
    