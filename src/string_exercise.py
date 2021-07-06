class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        txt = input_str[::-1]
        return txt

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        a = False
        if(character in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')):
            a = True
        return a

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        a1=sentence.split(" ")
        longest_string = max(a1, key=len)
        return longest_string

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        a2=text.split(" ")
        a3=map(lambda i:len(i), a2)
        a4=list(a3)
        return a4