from word_frequency import WordFrequency


# -------------------------------------------------
# Base class for dictionary implementations. DON'T CHANGE THIS FILE.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# -------------------------------------------------

class BaseDictionary:
    def build_dictionary(self, words_frequencies: [WordFrequency]):
        for word_frequency in words_frequencies:
            self.add_word_frequency(word_frequency)

    def search(self, word: str) -> int:
        if word in self._words_frequencies:
            return self._words_frequencies[word].frequency
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        if word_frequency.word in self._words_frequencies:
            return False
        self._words_frequencies[word_frequency.word] = word_frequency
        return True

    def delete_word(self, word: str) -> bool:
        if word not in self._words_frequencies:
            return False
        del self._words_frequencies[word]
        return True

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        words = []
        for word, word_frequency in self._words_frequencies.items():
            if word.startswith(prefix_word):
                words.append(word_frequency)
        words.sort(key=lambda word_frequency: word_frequency.frequency, reverse=True)
        return words[:3]
