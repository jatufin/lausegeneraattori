import sys

class SentenceGeneratorUI:
    def __init__(self, sentence_generator):
        self._sg = sentence_generator
        self._max_degree = 5
        self._degree = 2
        
    def launch(self):
        print("Main menu")

    def _read_text(self,textfile):
        print(f"Input file: {textfile}")
            
    def _genarate_sentence(self,degree=2, keywords=[]):
        print(f"Markov degree: {degree}")
        print(f"Keyword(s): {keywords}")

