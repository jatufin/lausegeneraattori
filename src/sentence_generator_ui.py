import sys

class SentenceGeneratorUI:
    def __init__(self, sentence_generator):
        self._sg = sentence_generator
        
    def launch(self):
        print("Main menu")

    def _read_text(self,textfile):
        print(f"Input file: {textfile}")
            
    def _genarate_sentence(self,degree=2, keywords=[]):
        print(f"Markov degree: {degree}")
        print(f"Keyword(s): {keywords}")

