import sys

from node import Node
from sentence_generator_ui import SentenceGeneratorUI

class SentenceGenerator:
    """
    Generate random sentences based on given text using Markov chains
    """
    def __init__(self, degree=5):
        """ Argument: degree is the maximum Markov degree, which can be used in text generation
            The depth of th tree will be degree+1
        """
        self._degree = degree
        self._tree = Node()

    @property
    def degree(self):
        return self._degree
    
    def read_text(self, filename):
        """ Read and process the give text file """
        pass

    def generate(self, degree, wordlist=[]):
        pass

    def read_string(self, input_string):
        token_list = self._clean_string(input_string).split(" ")
        self._insert_token_list(token_list)

    def print_tree(self):
        self._tree.print_tree()
        
    def _clean_string(self, s):
        return s

    def _insert_token_list(self, token_list):
        if token_list == []:
            return
            
        if len(token_list) < (self._degree + 1):
            self._tree.add_token_list(token_list)
        else:
            self._tree.add_token_list(token_list[:self._degree+1])
        self._insert_token_list(token_list[1:])

    def __str__(self):
        return "DEG: " + str(self.degree) + " ROOT" + str(self._tree)

    def _test(self):
        s = "aa bb cc aa bb aa bb"
        print(f"String: '{s}'")
        self.read_string(s)
        self.print_tree()
        print(str(self._tree._get_children_by_beginning(["aa", "bb"])))
    
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
    
    if argc == 0:
        ui = SentenceGeneratorUI(sg)
        ui.launch()
    elif argc == 1:
        if args[0] == "--test":
            sg._test()
        else:
            sg.read_text(args[0])
            sg.generate()
    elif argc == 2:
        sg.read_text(args[0])
        sg.generate(degree=int(args[1]))
    elif argc > 2:
        sg.read_text(argc[0])
        sg.generate(degree=int(args[1],args[2:]))


    return 0
    
    



if __name__ == "__main__": main()
