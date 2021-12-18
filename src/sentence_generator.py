import sys

from node import Node
from trie import Trie
from sentence_generator_ui import SentenceGeneratorUI


class SentenceGenerator:
    """
    Generate random sentences based on given text using Markov chains

    Attributes:
        _MAX_LENGTH : Maximum length of words in generated sentence
        _max_degree : Maximum degree of Markov chains can be produced
        _tree : Node or Trie object
    """
    def __init__(self, tree, degree=5):
        """Constructor for the SentenceGenerator class
        
        Args:
            tree : Node or Trie object
            degree : Integer, maximum Markov degree
                     The depth of the tree will be degree+1
        """
        self._MAX_LENGTH = 100000
        self._max_degree = degree
        self._tree = tree

    @property
    def max_degree(self):
        """The tree generated will be max_degree+1 deep, and allows searches
        of maximum of max_degree Markov degree chains

        Returns:
            Integer
        """
        return self._max_degree
    
    def read_file(self, filename):
        """Read and process the given text file
        The resulting trie will be self._max_degree + 1 deep

        Args:
            filename : String

        Returns:
            True in success, False in failure.
        """

        s = ""
        try:
            with open(filename, "r") as file:
                s = file.read()
            file.close()
        except IOError:
            self.print_error(f"Tiedoston luku ei onnistu '{filename}'.")
            return False

        self.read_string(s)
        
        return True

    def read_string(self, input_string):
        """ Creates trie tree from single string input

        Args:
            input_string : String
        """
        self._tree.reset()  # Clear the tree
        token_list = self.string_to_wordlist(input_string)
        self._insert_token_list(token_list)

    def number_of_words_in_string(self, input_string):
        """ Counts number of words in the string after preprocessing

        Args:
            input_string : String

        Returns:
            Integer
        """
        words = self._clean_string(input_string).split()
        return len(words)

    def number_of_different_words_in_string(self, input_string):
        """ Counts number of different words in the string after preprocessing

        Args:
            input_string : String

        Returns:
            Integer
        """
        words = self.string_to_wordlist(input_string)
        dict= {}
        for word in words:
            dict[word] = 1

        return len(dict)

    def string_to_wordlist(self, input_string):
        """ Preprocess the input string and split it by whitespaces
        to a list a words

        Args:
            input_string : String

        Returns:
            List of strings
        """
        token_list = self._clean_string(input_string).split()

        return token_list
    
    def print_tree(self):
        """ Print the trie data structure on screen
        """
        self._tree.print_tree()
        
    def _clean_string(self, input_string):
        """ Prepare the input string for processing

        Args:
            input_string : String

        Returns:
            String
        """
        return_string = self._remove_illegal_characters(input_string)
        return_string = return_string.lower()
        
        return return_string

    def _remove_illegal_characters(self, text):
        """ Only listed letters and caharacters are allowed in the input

        Args:
            text : String
        """
        allowed_characters = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPWRSTUVWXYZÅÄÖ\n "
        return "".join(filter(lambda c: c in allowed_characters, text))
    
    def _insert_token_list(self, token_list):
        """ Takes list of words found from the input text, and inserts it to the tree root

        Args:
            text : String
        """
        if token_list == []:
            return

        for i in range(len(token_list)):
            self._tree.add_token_list(token_list[i:i+self._max_degree+1])
            
    def __str__(self):
        """ String representation of the whole tree
        maximum degree is added on the front of the string

        Returns:
            String
        """
        return "DEG: " + str(self._max_degree) + " ROOT" + str(self._tree)

    def _get_sentence_as_list(self, degree, length, keywords):
        """ Generates list of words starting with 'keywords' from the tree.
        Given Markov degree is used to generate the list

        Args:
            degree : Integer
            length : Integer
            keywords : List of strings

        Returns:
            List of strings
        """
        wordlist = self._tree.get_random_series_by_keywords(keywords, degree+1)
        if not wordlist or len(wordlist) == 0:
            return []

        if len(wordlist) == length:
            return wordlist

        if len(wordlist) > length:
            return wordlist[:length]
        
        while(not len(wordlist) == length):
            last_words = wordlist[-degree:]
            
            if not self._tree.is_valid_beginning(last_words):
                break
            
            words = self._tree.get_random_series_by_keywords(
                last_words, degree+1)
            last_word = words[-1]
            wordlist += [last_word]

        return wordlist
            
    def get_sentence(self, degree, length, keywords=[]):
        """ Gets a list of words from the tree and returns it as string,
        with capital first letter and a period in the end.

        Args:
            degree : Integer
            length : Integer
            keywords (optional) : List of strings

        Returns:
            Strings
        """
        words = self._get_sentence_as_list(degree, length, keywords)
        if len(words) == 0:
            return ""
        sentence = " ".join(words)   # no ending character included
        sentence = sentence.capitalize()  # capitalize first letter
        sentence += "."             # period to the end
        
        return sentence

    def is_degree_valid(self, degree):
        """ Checks if given degree can be used for generating sentences
        
        Args:
            degree : Integer

        Returns:
            Boolean
        """
        if degree > 0 and degree <= self.max_degree:
            return True
        return False

    def is_length_valid(self, length):
        return length > 0 and length < self._MAX_LENGTH
    
    def is_string_valid_degree(self, input_string):
        """ Checks if the string given can be used as degree for generating
        sentences

        Args:
            input_string : String

        Returns:
            Boolean
        """
        if not input_string.isdigit():
            return False

        degree = int(input_string)

        if not self.is_degree_valid(int(degree)):
            return False

        return True

    def is_string_valid_length(self, input_string):
        """ Checks if the string given can be used as degree for
        generating sentences

        Args:
            input_string : String

        Returns:
            Boolean
        """
        if not input_string.isdigit():
            return False

        degree = int(input_string)

        if not self.is_length_valid(int(degree)):
            return False

        return True
    
    def print_error(self, message):
        """ For error messages stderr output stream is used

        Args:
            message : String
        """
        print(f"Virhe: {message}", file=sys.stderr)


def main():
    """Main program for launching Sentence generator from command line
    
        Command line:
        
        1. Open interactive user interface:
        $ python3 sentence_generator.py
        
        2. Print random sentence based on given corpus text and default Markov degree
        $ python3 sentence_generator.py corpus.txt

        Error messages:
        * Reading file 'corpus.txt' failed

        3. Print random sentence based on given corpus text and Markov degree
        $ python3 sentence_generator.py corpus.txt degree

        Error messages:
        * Reading file 'corpus.txt' failed
        * Given degree is out of bounds

        4. Print random sentence based on given corpus binary file, Markov degree and word(s)
        $ python3 sentence_generator.py corpus.txt degree keyword(s)

        Error messages:
        * Reading file 'corpus.txt' failed
        * Given degree is out of bounds
        * Keyword was not found from the corpus text
        """
    
    args = sys.argv[1:]
    argc = len(args)
    # Node object is trie with children in hash tables (Python Dictionary)
    sg_node = SentenceGenerator(Node())
    # Trie object is trie with children in lists tables (Python List)
    sg_trie = SentenceGenerator(Trie())

    generators = (("Node class (Dictionary)", sg_node),
                  ("Trie class (List)", sg_trie))

    default_sg = sg_node
    default_length = 8

    if argc == 0:
        ui = SentenceGeneratorUI(generators)
        ui.launch()
    elif argc == 2:
        if default_sg.read_file(args[0]):
            print(default_sg.get_sentence(degree=int(args[1]), length=default_length))
    elif argc == 3:
        if (default_sg.read_file(args[0]) and
            default_sg.is_string_valid_degree(args[1]) and
            default_sg.is_string_valid_length(args[2])):
            print(default_sg.get_sentence(degree=int(args[1]), length=int(args[2])))
    elif argc > 3:
        if (default_sg.read_file(args[0]) and
            default_sg.is_string_valid_degree(args[1]) and
            default_sg.is_string_valid_length(args[2])):
            print(default_sg.get_sentence(degree=int(args[1]), length=int(args[2]), keywords=args[3:]))
        
    return 0


if __name__ == "__main__":
    main()
