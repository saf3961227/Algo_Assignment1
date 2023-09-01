
# -------------------------------------------------
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# -------------------------------------------------

# Class representing a word and its frequency
class WordFrequency:
    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency
        
    # Method to compare two WordFrequency objects based on their words
    def __lt__(self, other):
        return self.word < other.word