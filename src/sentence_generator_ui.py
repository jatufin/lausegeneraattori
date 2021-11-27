import sys

class SentenceGeneratorUI:
    def __init__(self, sentence_generator):
        self._sg = sentence_generator
        self._degree = 2
        self._filename = ""
        self._keywords = []
        
    def launch(self):
        while(True):
            self._print_main_menu()
            command = input()
            if command == "0": break;

            if command == "1":
                self._read_text()
                continue
            if command == "2":
                self._change_degree()
                continue
            if command == "3":
                self._get_keywords()
                continue
            if command == "4":
                self._print_data_structure()
                continue
            if command == "":
                self._print_sentence()
                continue

    def _read_text(self):
        print("Anna tiedoston nimi: ", end='')
        filename = input()
        if self._sg.read_file(filename):
            print("Tiedoston '{filename}' luku onnistui")
            self._filename = filename

    def _change_degree(self):
        print("Anna Markovin aste: ", end='')
        intstring = input()
        if not self._sg.is_string_valid_degree(intstring):
            return
        self._degree = int(intstring)
                       
    def _get_keywords(self):
        print("Anna sanat, joilla lause alkaa: ", end='')
        words = input()
        self._keywords = words.split()

    def _print_data_structure(self):
        self._sg.print_tree()

    def _print_sentence(self):
        while(True):
            print(self._sg.get_sentence(self._degree, self._keywords))
            print("<enter>=uusi lause, 0=paluu: ",end='')
            if input() == "0":
                break
        
    def _print_main_menu(self):
        filename = self._filename
        if filename == "": filename = "<ei valittu>"
        if len(self._keywords) > 0:
            keywords = " ".join(self._keywords)
        else:
            keywords = "<tyhjä>"
        degree = self._degree
        maxdegree = self._sg.max_degree
        
        print(f"""
*** Lausegeneraattori - päävalikko ***

Lähdeteksti: {filename}
Markov-aste: {degree}
Lauseen alku: {keywords}
Maksimiaste: {maxdegree}

1 - Lue tekstitiedosto
2 - Vaihda Markov-aste
3 - Anna lauseen aloittavat sanat
4 - Tulosta tietorakenne

0 - Lopeta

Valitse toiminto tai paina <enter> tuottaaksesi uuden lauseen: """, end='')

    def _generate_sentence(self,degree=2, keywords=[]):
        print(f"Markov degree: {degree}")
        print(f"Keyword(s): {keywords}")

