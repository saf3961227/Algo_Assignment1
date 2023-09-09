from .base_dictionary import BaseDictionary
from .word_frequency import WordFrequency
import time
import csv

class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        self.head = None  # Initialize the head of the linked list to None
        self.operation_data = []

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        for wf in words_frequencies:
            self.add_word_frequency(wf)  # Add each WordFrequency object to the linked list

    def search(self, word: str) -> int:
        start_time = time.perf_counter()  # Record the start time of the search operation
        current = self.head
        while current:
            if current.word_frequency.word == word:
                end_time = time.perf_counter()  # Record the end time of the search operation
                # Append the operation details to the operation data list
                self.operation_data.append(["Search", word, current.word_frequency.frequency, end_time - start_time])
                return current.word_frequency.frequency
            current = current.next
        end_time = time.perf_counter()
        self.operation_data.append(["Search", word, 0, end_time - start_time])
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        start_time = time.perf_counter()  # Record the start time of the add operation
        new_node = ListNode(word_frequency)
        if not self.head:
            self.head = new_node
            end_time = time.perf_counter()  # Record the end time of the add operation
            self.operation_data.append(["Add", word_frequency.word, word_frequency.frequency, end_time - start_time])
            return True
        if self.head.word_frequency.word == word_frequency.word:
            end_time = time.perf_counter()
            self.operation_data.append(["Add", word_frequency.word, word_frequency.frequency, end_time - start_time])
            return False
        current = self.head
        while current.next:
            if current.next.word_frequency.word == word_frequency.word:
                end_time = time.perf_counter()
                self.operation_data.append(["Add", word_frequency.word, word_frequency.frequency, end_time - start_time])
                return False
            current = current.next
        current.next = new_node
        end_time = time.perf_counter()
        self.operation_data.append(["Add", word_frequency.word, word_frequency.frequency, end_time - start_time])
        return True

    def delete_word(self, word: str) -> bool:
        start_time = time.perf_counter()  # Record the start time of the delete operation
        if not self.head:
            end_time = time.perf_counter()  # Record the end time of the delete operation
            self.operation_data.append(["Delete", word, "N/A", end_time - start_time])
            return False
        if self.head.word_frequency.word == word:
            self.head = self.head.next
            end_time = time.perf_counter()
            self.operation_data.append(["Delete", word, "N/A", end_time - start_time])
            return True
        current = self.head
        while current.next:
            if current.next.word_frequency.word == word:
                current.next = current.next.next
                end_time = time.perf_counter()
                self.operation_data.append(["Delete", word, "N/A", end_time - start_time])
                return True
            current = current.next
        end_time = time.perf_counter()
        self.operation_data.append(["Delete", word, "N/A", end_time - start_time])
        return False

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        start_time = time.perf_counter()  # Record the start time of the autocomplete operation
        current = self.head
        results = []
        while current:
            if current.word_frequency.word.startswith(prefix_word):
                results.append(current.word_frequency)
            current = current.next
        results.sort(key=lambda x: -x.frequency)
        end_time = time.perf_counter()  # Record the end time of the autocomplete operation
        self.operation_data.append(["Autocomplete", prefix_word, "N/A", end_time - start_time])
        return results[:3]

    def write_operation_data_to_csv(self, filename='data_collection_linkedlist.csv'):
        # Write the operation data to a CSV file
        with open(filename, 'w', newline='') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow(["Operation", "Word", "Frequency", "Time Taken"])
            data_writer.writerows(self.operation_data)



