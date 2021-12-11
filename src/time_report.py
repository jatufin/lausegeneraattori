import os
from timeit import default_timer as timer
from datetime import timedelta


def time_report(filename, generators):
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
            input_string = file.read()
            file.close()
    except IOError:
        self.print_error(f"Tiedoston luku ei onnistu '{filename}'.")
        return False

    first_generator = generators[0][1]

    words = first_generator.number_of_words_in_string(input_string)
    different_words = first_generator.number_of_different_words_in_string(input_string)

    print(f"Syötteessä on {words} sanaa.")
    print(f"Kielessä on {different_words} erilaista sanaa.")

    for generator in generators:
        generator_desc = generator[0]
        sg = generator[1]

        print("*************************************")
        Print(f("Generaattori: {generator_desc}"))

        print("Generating Trie-trees:")
        for degree in range(5):
              sg._max_degree = degree
              took_time = measure_time(lambda: sg.read_file(input_string))
              print(f"Depth: {degree} trie took seconds: {took_time}")
            
    

    
def measure_time(function):
    """ Runs the given argumentless function and returns its runtime in
    seconds. Uses timeit library, which takes account garbage collection.
    """
    start = timer()
    function()
    end = timer()

    return timedelta(seconds=end - start)

