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
        token_list = self._clean_string(input_string).split()
        self._insert_token_list(token_list)

    def print_tree(self):
        self._tree.print_tree()
        
    def _clean_string(self, s):
        s = self._add_ending_period(s)
        s = self._remove_illegal_characters(s)
        s = self._add_spaces(s)
        s = s.lower()
        
        return s

    def _add_ending_period(self, s):
        return s + "."

    def _remove_illegal_characters(self, text):
        allowed_characters = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPWRSTUVWXYZÅÄÖ!?.\n "
        return "".join(filter(lambda c: c in allowed_characters, text))

    def _add_spaces(self, s):
        s = s.replace(".", " . ")
        s = s.replace("!", " ! ")
        s = s.replace("?", " ? ")            

        return s

    def _is_end_character(self, s):
        return s == "." or s == "!" or s == "?"
    
    def _insert_token_list(self, token_list):
        print(f"sentence_generator.py INSERT TOKEN LIST: {token_list}")
        if token_list == []:
            return

        ###### Recursive solution:
        # if len(token_list) < (self._max_degree + 1):
        #    self._tree.add_token_list(token_list)
        # else:
        #    self._tree.add_token_list(token_list[:self._max_degree+1])
        # self._insert_token_list(token_list[1:])

        ###### Iterative solution:        
        for i in range(len(token_list)):
            self._tree.add_token_list(token_list[i:i+self._max_degree+1])
            
    def __str__(self):
        return "DEG: " + str(self._max_degree) + " ROOT" + str(self._tree)

    def _get_sentence_as_list(self, keywords, degree):
        wordlist = self._tree.get_random_series_by_keywords(keywords, degree+1)
        if not wordlist or len(wordlist) == 0:
            return []
        
        while(not self._is_end_character(wordlist[-1])):
            last_words = wordlist[-degree:]
            words = self._tree.get_random_series_by_keywords(last_words, degree+1)
            last_word = words[-1]
            wordlist += [last_word]

        return wordlist
            
    def get_sentence(self, degree, keywords=[]):
        words = self._get_sentence_as_list(keywords, degree)
        if len(words) == 0:
            return ""
        sentence = " ".join(words[:-1])  # no ending character included
        sentence = sentence.capitalize() # capitalize first letter
        sentence += words[-1]            # ending character
        return sentence

    def is_degree_valid(self, degree):
        if degree > 0 and degree <= self.max_degree:
            return True
        return False

    def is_string_valid_degree(self, intstring):
        if not intstring.isdigit():
            self.print_error("Aste ei ole luonnollinen luku")
            return False
        degree = int(intstring)
        if not self.is_degree_valid(int(degree)):
            self.print_error("Asteen arvo ei ole sallitulla välillä")
            return False
        return True
        
    def print_error(self, message):
        print(f"Virhe: {message}", file=sys.stderr)
    
    def _test(self):
        s = "aa bb cc .aa bb aa bb. bb cc aa "
        print(f"String: '{s}'")
        self.read_string(s)
        self.print_tree()
        print("Children for ['aa', 'bb']: ", end='')
        print(str(self._tree._get_node_by_beginning(["aa", "bb"])))
        print("Random series 3 deep: ", end='')
        print(self._tree.get_random_series(3))
        print("Random series by keywords 3 deep: ", end='')
        print(self._tree.get_random_series_by_keywords(["aa", "bb"], 3))

        print("Random sentence with keywords 2 deep ['aa', 'bb']: ", end='')
        print(self._get_sentence_as_list(["aa", "bb"], 2))

        print("Get another sentence as text, degree 3, no keywords: ", end='')
        print(self.get_sentence(2))
        
        print("Valid beginning ['aa', 'bb']: ", end='')
        print(self._tree.is_valid_beginning(["aa", "bb"]))
        print("Valid beginning ['aa', 'cc']: ", end='')
        print(self._tree.is_valid_beginning(["aa", "cc"]))
        print("Open file 'test.txt': ", end='')
        if self.read_file("teZt.txt") == False:
            print("Failed")
        else:
            print("Succeed")
            self.print_tree()
        
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
    
    if argc == 0:
        ui = SentenceGeneratorUI(sg)
        ui.launch()
    elif argc == 1:
        if args[0] == "--test":
            sg._test()
        else:
            if sg.read_file(args[0]):
                print(sg.get_sentence(degree=default_degree))
    elif argc == 2:
        if sg.read_file(args[0]) and sg.is_string_valid_degree(args[1]):
            print(sg.get_sentence(degree=int(args[1])))

    elif argc > 2:
        if sg.read_file(args[0]) and sg.is_string_valid_degree(args[1]):
            print(sg.get_sentence(degree=int(args[1]), keywords=args[2:]))
        
    return 0
    
    



if __name__ == "__main__": main()
