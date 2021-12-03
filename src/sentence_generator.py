import sys

from node import Node
from sentence_generator_ui import SentenceGeneratorUI


class SentenceGenerator:
    """
    Generate random sentences based on given text using Markov chains
    """
    def __init__(self, degree=5):
        """ Argument: degree is the maximum Markov degree, which can be used in text generation
            The depth of the tree will be degree+1
        """
        self._max_degree = degree
        self._tree = Node()

    @property
    def max_degree(self):
        """ The tree generated will be max_degree+1 deep, and allows searches
        of maximum of max_degree Markov degree chains
        """
        return self._max_degree
    
    def read_file(self, filename):
        """ Read and process the given text file
        The resulting trie will be self._max_degree + 1 deep
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
        """
        token_list = self._clean_string(input_string).split()
        self._insert_token_list(token_list)

    def print_tree(self):
        """ Print the trie data structure on screen
        """
        self._tree.print_tree()
        
    def _clean_string(self, s):
        """ Prepare the input string for processing
        """
        s = self._remove_illegal_characters(s)
        s = s.lower()
        
        return s

    def _remove_illegal_characters(self, text):
        """ Only listed letters and caharacters are allowed in the input
        """
        allowed_characters = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPWRSTUVWXYZÅÄÖ\n "
        return "".join(filter(lambda c: c in allowed_characters, text))
    
    def _insert_token_list(self, token_list):
        """ Takes list of words found from the input text, and inserts it to the tree root
        """
        if token_list == []:
            return

        # Recursive solution:
        # if len(token_list) < (self._max_degree + 1):
        #    self._tree.add_token_list(token_list)
        # else:
        #    self._tree.add_token_list(token_list[:self._max_degree+1])
        # self._insert_token_list(token_list[1:])

        # Iterative solution:        
        for i in range(len(token_list)):
            self._tree.add_token_list(token_list[i:i+self._max_degree+1])
            
    def __str__(self):
        """ String representation of the whole tree
        maximum degree is added on the fron of the string
        """
        return "DEG: " + str(self._max_degree) + " ROOT" + str(self._tree)

    def _get_sentence_as_list(self, degree, length, keywords):
        """ Generates list of words starting with 'keywords' from the tree.
        Given Markov degree is used to generate the list
        """
        wordlist = self._tree.get_random_series_by_keywords(keywords, degree+1)
        if not wordlist or len(wordlist) == 0:
            return []
        
        while(not len(wordlist) == length):
            last_words = wordlist[-degree:]
            words = self._tree.get_random_series_by_keywords(
                last_words, degree+1)
            last_word = words[-1]
            wordlist += [last_word]

        return wordlist
            
    def get_sentence(self, degree, length, keywords=[]):
        """ Gets a list of words from the tree and returns it as string
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
        """
        if degree > 0 and degree <= self.max_degree:
            return True
        return False

    def is_length_valid(self, length):
        return length > 0
    
    def is_string_valid_degree(self, intstring):
        """ Checks if the string given can be used as degree for generating sentences
        """
        if not intstring.isdigit():
            self.print_error("Aste ei ole luonnollinen luku")
            return False
        degree = int(intstring)
        if not self.is_degree_valid(int(degree)):
            self.print_error("Asteen arvo ei ole sallitulla välillä")
            return False
        return True

    def is_string_valid_length(self, intstring):
        """ Checks if the string given can be used as degree for generating sentences
        """
        if not intstring.isdigit():
            self.print_error("Pituus ei ole luonnollinen luku")
            return False
        degree = int(intstring)
        if not self.is_length_valid(int(degree)):
            self.print_error("Pituuden arvo ei ole sallitulla välillä")
            return False
        return True
    
    def print_error(self, message):
        """ For error messages stderr output stream is used
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
    sg = SentenceGenerator()
    default_degree = 2
    default_length = 8

    if argc == 0:
        ui = SentenceGeneratorUI(sg)
        ui.launch()
    elif argc == 2:
        if sg.read_file(args[0]):
            print(sg.get_sentence(degree=int(args[1]), length=default_length))
    elif argc == 3:
        if (sg.read_file(args[0]) and
            sg.is_string_valid_degree(args[1]) and
            sg.is_string_valid_length(args[2])):
            print(sg.get_sentence(degree=int(args[1]), length=int(args[2])))
    elif argc > 3:
        if (sg.read_file(args[0]) and
            sg.is_string_valid_degree(args[1]) and
            sg.is_string_valid_length(args[2])):
            print(sg.get_sentence(degree=int(args[1]), length=int(args[2]), keywords=args[3:]))
        
    return 0


if __name__ == "__main__":
    main()
