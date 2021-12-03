import os


class SentenceGeneratorUI:
    def __init__(self, sentence_generators):
        self._generators = sentence_generators
        self._selected_generator = None
        self._sg = None
        self._degree = 2
        self._length = 8
        self._directory = "./text"
        self._filename = ""
        self._keywords = []

        self._set_generator(0)
        
    def launch(self):
        """ Main loop for the UI main menu
        """
        while(True):
            self._print_main_menu()
            command = input()
            if command == "0":
                break

            if command == "1":
                self._read_text()
                continue
            if command == "2":
                self._change_generator()
                continue
            if command == "3":
                self._change_degree()
                continue
            if command == "4":
                self._get_keywords()
                continue
            if command == "5":
                self._change_length()
                continue
            if command == "6":
                self._print_data_structure()
                continue
            if command == "":
                self._print_sentence()
                continue

    def _read_text(self):
        """ User enters the text file name and program processes it
        """
        file_names = os.listdir(self._directory)
        selection = self._list_selector(file_names,
                                        "Valitse tiedosto",
                                        selected=-1)
        if selection:
            filename = self._directory + "/" + file_names[selection]
            self._read_file(filename)

    def _read_file(self, filename):
        print(f"Reading and processing file {filename}")
        if self._sg.read_file(filename):
            print(f"Tiedoston '{filename}' luku onnistui")
            self._filename = filename

    def _change_generator(self):
        generator_descriptions = list(map(lambda x: x[0], self._generators))
        selection = self._list_selector(generator_descriptions,
                                        "Valitse luokka",
                                        selected=self._selected_generator)
        if selection:
            self._set_generator(selection)        

    def _list_selector(self, items, prompt, selected=-1):
        i = 0
        for item in items:
            if i == selected:
                print("*", end='')
            else:
                print(" ", end='')
            print(f"{i} {item}")
            i += 1
        print(f"\n{prompt}: ", end='')
        selection = input()
        if not selection.isdigit():
            return None
        index = int(selection)
        if index < 0 or index >= len(items):
            return None
        return index
    
    def _change_degree(self):
        """ Change the Markov degree which is used for generating sentences
        """
        print("Anna Markovin aste: ", end='')
        intstring = input()
        if not self._sg.is_string_valid_degree(intstring):
            return
        self._degree = int(intstring)

    def _set_generator(self, index_number):
        if index_number >= 0 and index_number < len(self._generators):
            self._selected_generator = index_number
            self._sg = self._generators[index_number][1]
            if self._filename:
                self._sg.read_file(self._filename)
            
    def _change_length(self):
        """ Change the Markov degree which is used for generating sentences
        """
        print("Anna haluttu lauseen pituus sanoina: ", end='')
        intstring = input()
        if not self._sg.is_string_valid_length(intstring):
            return
        self._length = int(intstring)
                       
    def _get_keywords(self):
        """ User enters the starting words the generated sentence should start
        """
        print("Anna sanat, joilla lause alkaa: ", end='')
        words = input()
        self._keywords = words.split()

    def _print_data_structure(self):
        """ Print the structure of the trie tree on screen
        """
        self._sg.print_tree()

    def _print_sentence(self):
        """ Generate sentence after <enter> presses based on given text file,
        Markov degree and beginning words
        """
        while(True):
            print(self._sg.get_sentence(self._degree, self._length, self._keywords))
            print("<enter>=uusi lause, 0=paluu: ", end='')
            if input() == "0":
                break
        
    def _print_main_menu(self):
        """ Main menu shows values of current text file, Markov degree and keywords.
        Also maximu degree which can be used is shown.
        """
        directory = self._directory
        filename = self._filename
        if filename == "":
            filename = "<ei valittu>"
        if len(self._keywords) > 0:
            keywords = " ".join(self._keywords)
        else:
            keywords = "<tyhjä>"
        generator = self._generators[self._selected_generator][0]
        degree = self._degree
        maxdegree = self._sg.max_degree
        length = self._length
        
        print(f"""
**************************************
*** Lausegeneraattori - päävalikko ***

Hakemisto: {directory}
Tiedosto: {filename}
Valittu generaattori: {generator}
Markov-aste: {degree}
Lauseen alku: {keywords}
Lauseen pituus: {length} sanaa
Maksimiaste: {maxdegree}

1 - Aseta ja lue tiedosto
2 - Vaihda generaattoria
3 - Vaihda Markov-aste
4 - Anna lauseen aloittavat sanat
5 - Anna haluttu lauseen pituus
6 - Tulosta tietorakenne

0 - Lopeta

Valitse toiminto tai paina <enter> tuottaaksesi uuden lauseen: """, end='')

    def _generate_sentence(self, degree=2, keywords=[]):
        """ Used for debugging
        """
        print(f"Markov degree: {degree}")
        print(f"Keyword(s): {keywords}")

