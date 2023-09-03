from .base_dictionary import BaseDictionary
from .word_frequency import WordFrequency


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

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        for wf in words_frequencies:
            self.add_word_frequency(wf)  # Add each WordFrequency object to the linked list

    def search(self, word: str) -> int:
        current = self.head
        while current:
            if current.word_frequency.word == word:
                return current.word_frequency.frequency  # Return the frequency of the word if found
            current = current.next
        return 0  # Return 0 if the word is not found

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        new_node = ListNode(word_frequency)
        if not self.head:
            self.head = new_node  # Set the head to the new node if the linked list is empty
            return True
        if self.head.word_frequency.word == word_frequency.word:
            return False  # Return False if the word is already present in the linked list
        current = self.head
        while current.next:
            if current.next.word_frequency.word == word_frequency.word:
                return False  # Return False if the word is already present in the linked list
            current = current.next
        current.next = new_node  # Add the new node to the end of the linked list
        return True

    def delete_word(self, word: str) -> bool:
        if not self.head:
            return False  # Return False if the linked list is empty
        if self.head.word_frequency.word == word:
            self.head = self.head.next  # Remove the head of the linked list if it contains the word
            return True
        current = self.head
        while current.next:
            if current.next.word_frequency.word == word:
                current.next = current.next.next  # Remove the node containing the word
                return True
            current = current.next
        return False  # Return False if the word is not found in the linked list

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        current = self.head
        results = []
        while current:
            if current.word_frequency.word.startswith(prefix_word):
                results.append(current.word_frequency)  # Add the WordFrequency object to the results if the word starts with the prefix
            current = current.next
        results.sort(key=lambda x: -x.frequency)  # Sort the results in descending order of frequency
        return results[:3]  # Return the top 3 results



