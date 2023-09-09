#dictionary. --- remember to change this
from .word_frequency import WordFrequency
from .base_dictionary import BaseDictionary
import bisect
import time
import csv


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
        self.operation_data = []

    # Builds the dictionary from a list of WordFrequency objects.
    def build_dictionary(self, words_frequencies: [WordFrequency]):
        self.words_frequencies = words_frequencies
        # Sort the list of WordFrequency objects by word.
        self.words_frequencies.sort(key=lambda x: x.word)

    # Searches for a word in the dictionary and returns its frequency.
    # Returns 0 if the word is not found.
    def search(self, word: str) -> int:
        start_time = time.perf_counter()
        
        # Find the index of the word in the list.
        idx = bisect.bisect_left(self.words_frequencies, WordFrequency(word, 0))
        
        # Check if the word is in the list.
        if idx != len(self.words_frequencies) and self.words_frequencies[idx].word == word:
            frequency = self.words_frequencies[idx].frequency
        else:
            frequency = 0
        
        end_time = time.perf_counter()
        operation_time = end_time - start_time
        
        self.operation_data.append(["Search", word, frequency, operation_time])
        
        return frequency


    # Adds a WordFrequency object to the dictionary.
    # Returns False if the word is already in the dictionary, True otherwise.
    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        # Record the start time of the operation
        start_time = time.perf_counter()
        
        # Find the index where the word_frequency object should be inserted
        idx = bisect.bisect_left(self.words_frequencies, word_frequency)
        
        # Check if the word is already in the list
        if idx != len(self.words_frequencies) and self.words_frequencies[idx].word == word_frequency.word:
            result = False
        else:
            # Insert the word_frequency object in the list
            bisect.insort(self.words_frequencies, word_frequency)
            result = True
        
        # Record the end time of the operation
        end_time = time.perf_counter()
        
        # Calculate the time taken for the operation
        operation_time = end_time - start_time
        
        # Append the operation data to the operation_data list
        self.operation_data.append(["Add", word_frequency.word, word_frequency.frequency, operation_time])
        
        # Return the result of the operation
        return result

    def delete_word(self, word: str) -> bool:
        # Record the start time of the operation
        start_time = time.perf_counter()
        
        # Find the index of the word in the list
        idx = bisect.bisect_left(self.words_frequencies, WordFrequency(word, 0))
        
        # Check if the word is in the list and delete it if found
        if idx != len(self.words_frequencies) and self.words_frequencies[idx].word == word:
            del self.words_frequencies[idx]
            result = True
        else:
            result = False
        
        # Record the end time of the operation
        end_time = time.perf_counter()
        
        # Calculate the time taken for the operation
        operation_time = end_time - start_time
        
        # Append the operation data to the operation_data list
        self.operation_data.append(["Delete", word, "N/A", operation_time])
        
        # Return the result of the operation
        return result

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        # Record the start time of the operation
        start_time = time.perf_counter()
        
        # Find the index of the first word that matches the prefix
        idx = bisect.bisect_left(self.words_frequencies, WordFrequency(prefix_word, 0))
        results = []
        
        # Find all words that start with the prefix and add them to the results list
        while idx < len(self.words_frequencies) and self.words_frequencies[idx].word.startswith(prefix_word):
            results.append(self.words_frequencies[idx])
            idx += 1
        
        # Sort the results by frequency in descending order and return the top 3
        results.sort(key=lambda x: -x.frequency)
        
        # Record the end time of the operation
        end_time = time.perf_counter()
        
        # Calculate the time taken for the operation
        operation_time = end_time - start_time
        
        # Append the operation data to the operation_data list
        self.operation_data.append(["Autocomplete", prefix_word, "N/A", operation_time])
        
        # Return the top 3 results
        return results[:3]

    
    def write_operation_data_to_csv(self, filename='data_collection.csv'):
        with open(filename, 'w', newline='') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow(["Operation", "Word", "Frequency", "Time Taken"])
            data_writer.writerows(self.operation_data)