#add dictionary back
from .base_dictionary import BaseDictionary
from .word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        self.root = TrieNode()

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        for wf in words_frequencies:
            self.add_word_frequency(WordFrequency(wf.word, wf.frequency))


    def search(self, word: str) -> int:
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return 0
        if node.is_last:
            return node.frequency
        return 0


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:

        node = self.root
        for letter in word_frequency.word:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]
        if node.is_last:
            return False
        node.is_last = True
        node.frequency = word_frequency.frequency
        return True
        

    def delete_word(self, word: str) -> bool:
        node = self.root
        
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
            
        if node.is_last:
            node.is_last = False
            node.frequency = None
            return True
        
        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        completions = []

    # Find the node corresponding to the prefix
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return completions

    # Helper function to perform Trie traversal and find completions
        def find_completions(node, prefix):
            if node.is_last:
                completions.append(WordFrequency(prefix, node.frequency))
            for letter, child in node.children.items():
                find_completions(child, prefix + letter)

        if node.is_last:
            completions.append(WordFrequency(word, node.frequency))

        find_completions(node, word)
    
    # Sort completions by frequency in descending order and return the top 3
        completions.sort(key=lambda x: x.frequency, reverse=True)
        return completions[:3]
