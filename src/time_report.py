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
        print(f"Generaattori: {generator_desc}")

        print("Luodaan eri syvyisiä Trie-puita:")
        for degree in range(7):            
            sg._max_degree = degree
            took_time = measure_time(lambda: sg.read_string(input_string))
            print(f"  Puun syvyys: {degree+1} Kulunut aika sekunteina: {took_time}")
        # The last generated depth remains in the generators

        for degree in range(1, 6):
            print(f"Markovin aste: {degree}")
            for sentence_length in range(6, 16):
                count = 100
                took_time = measure_time(lambda: generate_sentences(generator=sg,
                                                                    degree=degree,
                                                                    length=sentence_length,
                                                                    count=count))
                print(f"  Tuotettiin {count} lausetta, pituudeltaan {sentence_length} sanaa, ajassa: (sekunteja) {took_time}")

                
def measure_time(function):
    """ Runs the given argumentless function and returns its runtime in
    seconds. Uses timeit library, which takes account garbage collection.
    """
    start = timer()
    function()
    end = timer()

    return timedelta(seconds=end - start)


def generate_sentences(generator, degree=2, count=50, length=10):
    for i in range(count):
        generator.get_sentence(degree=degree, length=length)
    
