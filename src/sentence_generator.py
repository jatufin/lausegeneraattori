from node import Node

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

    def save(self, filename):
        """ Save the current data structure to binary file """
        pass
    
    def load(self, filename):
        """ Load a previously saved binary file """
        pass

    def generate(self, degree, wordlist=[]):
        pass

    def read_string(self, input_string):
        token_list = self._clean_string(input_string).split(" ")
        self._insert_token_list(token_list)

    def print(self):
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

