import sys

def launch_ui():
    print("Launch interactive user interface")

def text_to_bin(textfile, binaryfile):
    print(f"Input file: {textfile}")
    print(f"Output file: {binaryfile}")

def print_sentence(binaryfile, degree=2, keywords=[]):
    print(f"Input file: {binaryfile}")
    print(f"Markov degree: {degree}")
    print(f"Keyword(s): {keywords}")

def main():
    """Main program for launching Sentence generator from command line

    Command line:

    1. Open interactive user interface:
        $ python3 sentence_generator.py

    2. Process corpus text and create binary file:
        $ python3 sentence_generator.py --init corpus.txt corpus.da
       
       Error messages:
        * File 'corpus.txt' does not exist
        * File 'corpus.dat' already exists

    3. Print random sentence based on given corpus binary file and default Markov degree
        $ python3 sentence_generator.py corpus.dat

       Error messages:
        * Reading file 'corpus.dat' failed

    4. Print random sentence based on given corpus binary file and Markov degree
        $ python3 sentence_generator.py corpus.dat degree

       Error messages:
        * Reading file 'corpus.dat' failed
        * Given degree is out of bounds


    5. Print random sentence based on given corpus binary file, Markov degree and word(s)
        $ python3 sentence_generator.py corpus.dat degree keyword(s)

       Error messages:
        * Reading file 'corpus.dat' failed
        * Given degree is out of bounds
        * Keyword was not found from the corpus text
    """
    
    args = sys.argv[1:]
    argc = len(args)
    
    if argc == 0:
        launch_ui()
    elif args[0] == "--init":
        if argc != 3:
            sys.stderr.write("Wrong number of arguments")
            return(1)
        else:
            text_to_bin(args[1], args[2])
    elif argc == 1:
        print_sentence(binaryfile=args[0])
    elif argc == 2:
        print_sentence(binaryfile=args[0], degree=args[1])
    else:
        print_sentence(binaryfile=args[0], degree=args[1], keywords=args[2:])        

    return(0)
    
    

if __name__ == "__main__": main()
