"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """ Machine to find random words from a dictionary which is in a seperate text file.
    
    >>> wf = WordFinder("simplewords.txt")
    3 words read

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf.random() in ['aaaa', 'vvvv']
    False

    """ 

    def __init__(self, file_path):
        """ Calls the method file_open() """

        self.words = self.file_open(file_path)

    def __repr__(self):
        """ Show representation of the INSTANCE of WordFinder. """
        return f"<WordFinder words length={len(self.words)}>"

    def file_open(self, file_path):
        """ 
        Opens the file and reads the contents of it by skipping the blank spaces
        Returns the words read from the file  
        
        """
        file = open(file_path , 'r')
        words = [word.strip() for word in file]
        print(f"{len(words)} words read")
        file.close() 
        return words
    
    def random(self):
        """ Returns a random word from the words dictionary """
        return choice(self.words)

    
class SpecialWordFinder(WordFinder):
    """ 
    Specialized WordFinder that excludes blank lines/comments.

    >>> swf = SpecialWordFinder("complex.txt")
    4 words read

    >>> swf.random() in ['kale', 'parnships', 'apple', 'mango']
    True

    >>> swf.random() in ['aaaa', 'vvvv']
    False
    
    """ 

    def __repr__(self):
        """ Show representation of the INSTANCE of SpecialWordFinder. """
        return f"<SpecialWordFinder words length={len(self.words)}>"


    def file_open(self, file_path):
        """ 
        Opens the file and reads the contents of it by skipping the blank spaces/comments
        Returns the words read from the file 
        
        """
        file = open(file_path , 'r')

        words = [word.strip() for word in file if word.strip() and not word.startswith('#')]

        print(f"{len(words)} words read")
        file.close() 
        return words