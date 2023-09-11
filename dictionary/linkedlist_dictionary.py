from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
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
        current = self.head
        while current:
            if current.word_frequency.word == word:
                return current.word_frequency.frequency
            current = current.next
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        new_node = ListNode(word_frequency)
        if not self.head:
            self.head = new_node
            return True
        if self.head.word_frequency.word == word_frequency.word:
            return False
        current = self.head
        while current.next:
            if current.next.word_frequency.word == word_frequency.word:
                return False
            current = current.next
        current.next = new_node
        return True

    def delete_word(self, word: str) -> bool:
        if not self.head:
            return False
        if self.head.word_frequency.word == word:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.word_frequency.word == word:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        current = self.head
        results = []
        while current:
            if current.word_frequency.word.startswith(prefix_word):
                results.append(current.word_frequency)
            current = current.next
        results.sort(key=lambda x: -x.frequency)
        return results[:3]



