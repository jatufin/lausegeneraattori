import os
import random

from timeit import default_timer as timer
import datetime
from datetime import timedelta


def time_report(filename, generators):
    """Using given text file and sentence generators, which use
    different classes for trie structure (Node or Trie), run
    number of tests and generae CSV files for analyzing

    Args:
        filename : String. Name of the input text file
        generators : A list of SentenceGenerator objects

    Output files:

        trie_build,csv : Table of building times of tries from the input file. Columns:

            generator : String containing the description of the generator
            input_length : Integer, input text word count
            language_size : Integer, different word in the input text
            depth : Integer, depth of the trie tree which was built
            time : Integer, time it took to build the trie.

        sentence_generation.csv : Table of times it takes to generate different
                                  length sentences. Columns:

            generator : String containing the description of the generator
            input_length : Integer, input text word count
            language_size : Integer, different word in the input text
            markov_degree : Integer, Markov degree used to generate the sentence
            sentence_length : Ineteger, length in word of the generated sentence
            speed : Integer. Average sentences per second it ook to generate sentences
    """
    split_input = 5000 # word count of each input size increment
    number_of_sentences = 100
    min_sentence_length = 6
    max_sentence_length = 20
    max_markov_degree = 5
    
    if not generators:
        print("Ei generaattoreita")
        return
    
    print("Markovin ketjujen toteutukset: (Trie-puut):")

    for generator in generators:
        print(generator[0])

    print(f"Syötetiedosto: {filename}")
    
    input_string = ""
    try:
        with open(filename, "r") as file:
            file_content_string = file.read()
            file.close()
    except IOError:
        print(f"Tiedoston luku ei onnistu '{filename}'.")
        return False

    first_generator = generators[0][1]  # Just for the next line

    text_as_wordlist = first_generator.string_to_wordlist(file_content_string)
    number_of_words = first_generator.number_of_words_in_string(file_content_string)
    different_words = first_generator.number_of_different_words_in_string(file_content_string)

    metadata = f"# Date: {datetime.datetime.now()}\n"
    metadata += f"# Input file: {filename}\n"
    metadata += f"# Text length in words: {number_of_words}\n"
    metadata += f"# Different words in the text: {different_words}\n"

    csv_string_trie_build = metadata
    csv_string_trie_build += '"generator";"input_length";"language_size";"depth";"time"\n'

    csv_string_sentence_generation = metadata
    csv_string_sentence_generation += '"generator";"number_of_words";"markov_degree";"sentence_length";"speed"\n'
    
    for generator in generators:
        generator_desc = generator[0]
        sg = generator[1]

        print("*************************************")
        print(f"Generaattori: {generator_desc}")

        # Different input lengths
        words_from_start = 0
        while(words_from_start < len(text_as_wordlist)):
            words_from_start += split_input
            input_string = " ".join(text_as_wordlist[:words_from_start])
            number_of_words = sg.number_of_words_in_string(input_string)
            different_words = sg.number_of_different_words_in_string(input_string)
            print(f"Syötteen pituus {number_of_words} sanaa. Erilaisia sanoja: {different_words}")
            
            print("  Luodaan eri syvyisiä Trie-puita:")
            # Measure time it takes to generate tries of different depths
            for degree in range(max_markov_degree+1):            
                sg._max_degree = degree
                
                took_time = measure_time(lambda: sg.read_string(input_string))
                print(f"    Puun syvyys: {degree+1} Kulunut aika sekunteina: {took_time}")

                csv_line = f'"{generator_desc}";{number_of_words};{different_words};{degree+1};{took_time}\n'
                csv_string_trie_build += csv_line

            # Measure time it takes ito generate different length sentences with
            # different Markov degrees
            print(f"Luodaan lauseita. Syötteen pituus {number_of_words} sanaa. Erilaisia sanoja: {different_words}")
            for degree in range(1, max_markov_degree+1):
                print(f"    Lauseen luonti:{generator_desc} Markovin aste: {degree}")
                for sentence_length in range(min_sentence_length, max_sentence_length+1):
                    took_time = measure_time(lambda: generate_sentences(generator=sg,
                                                                        degree=degree,
                                                                        length=sentence_length,
                                                                        count=number_of_sentences))
                    speed = number_of_sentences / took_time
                    print(f"Tietorakenne: {generator_desc} Syöte {number_of_words} sanaa, Erilaisia sanoja: {different_words}, Markovin aste: {degree}, Luodun lauseen pituus: {sentence_length:2} Keskinopeus: {speed:6.0f} lausetta sekunnissa.")
                    csv_line = f'"{generator_desc}";{number_of_words};{degree};{sentence_length};{speed}\n'
                    csv_string_sentence_generation += csv_line

    # Write CSV files
    write_file("trie_build.csv", csv_string_trie_build)
    write_file("sentence_generation.csv", csv_string_sentence_generation)
    
def measure_time(function):
    """ Runs the given argumentless function and returns its runtime in
    seconds. Uses timeit library, which takes account garbage collection.
    """
    start = timer()
    function()
    end = timer()

    return timedelta(seconds=end - start).total_seconds()

def write_file(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
            file.close()
    except IOError:
        self.print_error(f"Tiedoston kirjoitus ei onnistu '{filename}'.")
        return False

    print(f"Tallennettiin tiedosto: '{filename}'")
    return True


def generate_test_text(filename="test.txt", size=50000, words=["aa", "aa", "bb"]):
    """ Produce test text file selecting random items from the wordlist
    """
    output_string = ""

    try:
        with open(filename, "w") as file:
            for i in range(size):
                next_word = random.choice(words)
                file.write(next_word)
                file.write(" ")
            file.close()
    except IOError:
        self.print_error(f"Tiedoston kirjoitus ei onnistu '{filename}'.")
        return False
    
    print(f"Tallennettiin tiedosto: '{filename}'")
    return True
    

        
        


def generate_sentences(generator, degree=2, count=50, length=10):
    for i in range(count):
        generator.get_sentence(degree=degree, length=length)
    
