import os
from timeit import default_timer as timer
from datetime import timedelta


def time_report(filename, generators):
    split_input = 1000 # word count of each input size increment
    number_of_sentences = 100
    min_sentence_length = 5
    max_sentence_length = 20
    max_markov_degree = 5
    
    if not generators:
        print("Ei generaattoreita")
        return
    
    print("Markovin ketjujen toteutukset: (Trie-puut):")

    for generator in generators:
        print(generator[0])

    # An instance for calling methdos

    
    print(f"Syötetiedosto: {filename}")
    
    input_string = ""
    try:
        with open(filename, "r") as file:
            file_content_string = file.read()
            file.close()
    except IOError:
        self.print_error(f"Tiedoston luku ei onnistu '{filename}'.")
        return False

    first_generator = generators[0][1] # Just for the next line
    text_as_wordlist = first_generator.string_to_wordlist(file_content_string)
    
    csv_string_trie_build = '"generator";"input_length";"language_size";"depth";"time"\n'
    csv_string_sentence_generation = '"generator";"input_length";"language_size";"markov_degree";"sentence_length";"speed"\n'
    
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
            print("Lista:")
            print(text_as_wordlist[:words_from_start])
            print("Stringi:")
            print(input_string)
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
                    print(f"Tietorakenne: {generator_desc} Syöte {number_of_words} sanaa, Erilaisia sanoja: {different_words}, Markovin aste: {degree}, Luodun lauseen pituus: {sentence_length:2} Keskinopeus: {speed:5.0f} lausetta sekunnissa.")
                    csv_line = '"{generator_desc}";{words};{different_words};{degree};{sentence_length};{speed}\n'
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

    
def generate_sentences(generator, degree=2, count=50, length=10):
    for i in range(count):
        generator.get_sentence(degree=degree, length=length)
    
