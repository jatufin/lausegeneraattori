class SentenceGenerator:
    """
    Generate random sentences based on given text using Markov chains
    """
    def __init__(self, degree=5):
        """ Argument: degree is the maximum Markov degree, which will be saved to the tree """
        self.degree = degree

    def readText(self, filename):
        """ Read and process the give text file """
        return filename

    def save(self, filename):
        """ Save the current data structure to binary file """
        return filename

    def load(self, filename):
        """ Load a previously saved binary file """
        return filename

    def generate(self, degree, wordlist=[]):
        ws = "" if wordlist == [] else " " + " ".join(wordlist)
        return degree + ws
