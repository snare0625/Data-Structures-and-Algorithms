'''
Count Word Frequency
Define a function to count the frequency of words in a given list of words.
'''

def count_word_frequency(words):
    word_frequencies = {}
    for word in words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies