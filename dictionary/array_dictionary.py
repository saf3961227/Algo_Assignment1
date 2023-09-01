#dictionary. --- remember to change this
from .word_frequency import WordFrequency
from .base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    # Constructor initializes an empty list of word frequencies.
    def __init__(self):
        self.words_frequencies = []

    # Builds the dictionary from a list of WordFrequency objects.
    def build_dictionary(self, words_frequencies: [WordFrequency]):
        self.words_frequencies = words_frequencies
        # Sort the list of WordFrequency objects by word.
        self.words_frequencies.sort(key=lambda x: x.word)

    # Searches for a word in the dictionary and returns its frequency.
    # Returns 0 if the word is not found.
    def search(self, word: str) -> int:
        # Find the index of the word in the list.
        idx = bisect.bisect_left(self.words_frequencies, WordFrequency(word, 0))
        # Check if the word is in the list.
        if idx != len(self.words_frequencies) and self.words_frequencies[idx].word == word:
            return self.words_frequencies[idx].frequency
        else:
            return 0

    # Adds a WordFrequency object to the dictionary.
    # Returns False if the word is already in the dictionary, True otherwise.
    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        idx = bisect.bisect_left(self.words_frequencies, word_frequency)
        if idx != len(self.words_frequencies) and self.words_frequencies[idx].word == word_frequency.word:
            return False
        else:
            bisect.insort(self.words_frequencies, word_frequency)
            return True

    # Deletes a word from the dictionary.
    # Returns True if the word was deleted, False otherwise.
    def delete_word(self, word: str) -> bool:
        idx = bisect.bisect_left(self.words_frequencies, WordFrequency(word, 0))
        if idx != len(self.words_frequencies) and self.words_frequencies[idx].word == word:
            del self.words_frequencies[idx]
            return True
        else:
            return False

    # Returns a list of up to 3 most frequent words in the dictionary that start with a prefix.
    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        idx = bisect.bisect_left(self.words_frequencies, WordFrequency(prefix_word, 0))
        results = []
        # Find all words that start with the prefix.
        while idx < len(self.words_frequencies) and self.words_frequencies[idx].word.startswith(prefix_word):
            results.append(self.words_frequencies[idx])
            idx += 1
        # Sort the results by frequency in descending order and return the top 3.
        results.sort(key=lambda x: -x.frequency)
        return results[:3]