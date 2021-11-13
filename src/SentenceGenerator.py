class SentenceGenerator:
    """
    Generate random sentences based on given text using Markov chains
    """
    def readText(self, filename):
        return filename
    
    def save(self, filename):
        return filename
    
    def load(self, filename):
        return filename
        
    def generate(self, degree, wordlist=[]):
        ws = "" if wordlist == [] else " " + " ".join(wordlist)
        return degree + ws 
    
    
