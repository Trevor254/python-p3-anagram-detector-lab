# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        """
        Initialize the Anagram class with a word.
        :param word: The word to use for finding anagrams.
        """
        self.word = word.lower()

    def match(self, possible_anagrams):
        """
        Find all anagrams of the word from the given list.
        :param possible_anagrams: List of potential anagrams.
        :return: List of words that are anagrams of the original word.
        """
        # Sort the characters of the word to create a standard representation
        sorted_word = sorted(self.word)

        # Filter and return matches where the sorted characters match and the words are not identical
        return [
            candidate for candidate in possible_anagrams
            if sorted(candidate.lower()) == sorted_word and candidate.lower() != self.word
        ]

# Example usage (for testing purposes):
if __name__ == "__main__":
    listen = Anagram("listen")
    print(listen.match(["enlists", "google", "inlets", "banana"]))  # Output: ['inlets']

