import os

from time_report import time_report
from output_diagnose import output_diagnose

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
            if command == "7":
                self._run_time_report()
                continue
            if command == "8":
                self._run_output_diagnose()
                continue        
            if command == "":
                self._print_sentence()
                continue

    def _read_text(self):
        """ User enters the text file name and program processes it
        """
        file_names = os.listdir(self._directory)
        selection = self._list_selector(file_names,
                                        "Valitse tiedosto (<enter>=paluu)",
                                        selected=-1)
        if not selection is None:
            filename = self._directory + "/" + file_names[selection]
            self._read_file(filename)

    def _read_file(self, filename):
        """ Reads and processes given file, if it succeeds, the
        user interfaces _filename property is updated and shown
        in the main menu.
        """
        print(f"Reading and processing file {filename}")
        if self._sg.read_file(filename):
            print(f"Tiedoston '{filename}' luku onnistui")
            self._filename = filename

    def _change_generator(self):
        """ More than one generator (Trie-tree implementations) can be used.
        They are provided in a list, which each element has first string
        describing the generator, and second the generator object itself.
        """
        generator_descriptions = list(map(lambda x: x[0], self._generators))
        selection = self._list_selector(generator_descriptions,
                                        "Valitse luokka",
                                        selected=self._selected_generator)

        if not selection == None:
            self._set_generator(selection)        

    def _list_selector(self, items, prompt, selected=-1):
        """ Prints a given list with numbers on each line, and asks user
        to select one. If selected argument is given, that line is
        higlighted with asterisk.
        """
        i = 1
        for item in items:
            if i == selected+1:  # Array starts from 0, selections 1
                print("*", end='')
            else:
                print(" ", end='')
            print(f"{i} {item}")
            i += 1
        print(f"\n{prompt}: ", end='')
        selection = input()
        if selection == "":
            if selected == -1:
                return None
            else:
                return selected
            
        if not selection.isdigit():
            return None
        index = int(selection) - 1

        if index < 0 or index >= len(items):
            return None
        return index
    
    def _change_degree(self):
        """ Change the Markov degree which is used for generating sentences
        """
        print("Anna Markovin aste: ", end='')
        intstring = input()
        if not self._sg.is_string_valid_degree(intstring):
            print("Arvo ei ollut sallituissa rajoissa")
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
            print("Arvo ei ollut sallituissa rajoissa")            
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

    def _run_time_report(self):
        """ Run tests with all Generators using given corpus file
        """
        time_report(self._filename , self._generators)
        
    def _run_output_diagnose(self):
        """Diagnose word frequencies in the output sentences
        """
        printout_options = ["None", "Partial", "Full"]
        selection = self._list_selector(printout_options,
                                        "Valitse tulostuksen taso",
                                        selected=2)

        if not selection == None:
            printout = printout_options[selection]
            print(f"Printout: {printout}")
            output_diagnose(self._filename,
                            self._sg,
                            printout)
        
    def _print_sentence(self):
        """ Generate sentence after <enter> presses based on given text file,
        Markov degree and beginning words
        """
        while(True):
            print(self._sg.get_sentence(self._degree,
                                        self._length,
                                        self._keywords))
            print("<enter>=uusi lause, 0=paluu: ", end='')
            if input() == "0":
                break
        
    def _print_main_menu(self):
        """ Main menu shows values of current text file, Markov degree and keywords.
        Also maximum degree which can be used is shown.
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
7 - Aja aikaraportti
8 - Aja tuotettujen lauseiden analyysi

0 - Lopeta

Valitse toiminto tai paina <enter> tuottaaksesi uuden lauseen: """, end='')

    def _generate_sentence(self, degree=2, keywords=[]):
        """ Used for debugging
        """
        print(f"Markov degree: {degree}")
        print(f"Keyword(s): {keywords}")

