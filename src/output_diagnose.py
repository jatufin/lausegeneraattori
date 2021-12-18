

def output_diagnose(filename, sg, printout="Full"):
    """Using given input text generate sentences with different Markov
    degrees, and analyze if the words appear in the excepted probability.
    Output is written to stdout.

    Example:
        A sentence generated with 2nd degree Markov chain is:
        "aa bb cc bb dd aa bb cc aa bb aa"
        
        All two word long prefixes, except the last one,
         are searched from the original text:
        "aa bb", "bb cc", "cc bb", "bb dd", "dd aa"
 
        Occurences of different words after the prefixes is counted
        from the original text. That is compared to the occurences
        of words in the generated sentence:
 
        "aa bb" is followed by "cc" 67% and "aa"" 33 times.

        Enough sentences will be generated, to get valid sampling.

    Args:
        filename : String. Name of the input text file
        sg : SentenceGenerator

    """
    max_markov_degree = sg.max_degree
    sentence_length = 10
    number_of_sentences = 10000
    
    print(f"Syötetiedosto: {filename}")
    
    try:
        with open(filename, "r") as file:
            file_content_string = file.read()
            file.close()
    except IOError:
        print(f"Tiedoston luku ei onnistu '{filename}'.")
        return False

    if not printout == "None":
        print(f"Filename: {filename}")
        
    text_as_wordlist = sg.string_to_wordlist(file_content_string)

    sg.read_string(file_content_string)

    csv_list = ['"filename";"degree";"sentence_length";"number_of_sentences";"difference"\n']

    i = 0
    while(i < number_of_sentences):
        i += 500
        result = all_degrees(sg,
                             sentence_length=sentence_length,
                             number_of_sentences=i,
                             text_as_wordlist=text_as_wordlist,
                             csv_row_prefix=f"{filename};",
                             printout=printout)
        csv_list += result

    save_csv_to_file("output_diagnose.csv", csv_list)
    

def save_csv_to_file(filename, csv_list):
    try:
        with open(filename, "w") as file:
            for row in csv_list:
                file.write(row)
            file.close()
    except IOError:
        self.print_error(f"Tiedoston kirjoitus ei onnistu '{filename}'.")
        return False

    print(f"Tallennettiin tiedosto: '{filename}'")
    return True

def all_degrees(sg, sentence_length, number_of_sentences, text_as_wordlist, csv_row_prefix, printout):
    """Generate sentences with all markov degrees from 0 to max_degree, and compare
    occurences of words following degree length prefixes to those of full text.

    Args:
        sg : SentenceGenerator
        sentence_length : Number of words in the generated senteces
        text_as_wordlist : List of strings containing the original text.
        csv_row_prefix : String added to the start of each CSV row
        printout : String. If "Full" print to stdout progress of the process

    Returns:
        List of strings containing end of rows for the CSV file
    """
    return_list = []
    
    for degree in range(0, sg.max_degree+1):

        # generate number of sentences and count number of occurences of words
        # after markov degree long prefixes
        prefixes_in_sentences = get_occurences_for_number_of_sentences(sg,
                                                                       degree,
                                                                       sentence_length,
                                                                       number_of_sentences)

        difference_to_full_text = compare_occurences_in_sentences_to_full_text(text_as_wordlist,
                                                                               prefixes_in_sentences,
                                                                               printout)

        if not printout == "None":
            print(f"Degree: {degree} length: {sentence_length} Number of sentences: {number_of_sentences} Difference: {difference_to_full_text:2.5}")
        return_list.append(csv_row_prefix + f"{degree};{sentence_length};{number_of_sentences};{difference_to_full_text}\n")

    return return_list

        
def get_occurences_for_number_of_sentences(sg,
                                           degree,
                                           sentence_length,
                                           number_of_sentences):
    """Generate number of sentences and collect number of occurences
    of words after Markov degree long prefixes
    The return value is produced by running method
    get_following_word_occurences_for_all_prefixes()
    for each generated sentence.

    Args:
        sg : SentenceGenerator
        degree : Integer. Markov degree, which is used as the length of the prefixes
    sentence_length : Integer. Sentence length in words.
        number_of_sentences : Integer. How many sentences should be generated

    Returns:
        Dictionary, where prefixes as tuples are keys and values are
        dictionaries, where strings (words) are keys and their occurences
        are integer values.
    """
    prefix_dict = {}
    
    for i in range(number_of_sentences):
        sentence = sg._get_sentence_as_list(degree=degree,
                                            length=sentence_length,
                                            keywords=[])
        result = get_following_word_occurences_for_all_prefixes(sentence, degree)
        sum_occurences_for_multiple_prefixes(prefix_dict, result)

    return prefix_dict
    

def compare_occurences_in_sentences_to_full_text(text_as_wordlist,
                                                 prefixes_in_sentences,
                                                 printout="Full"):
    """Get the original input text as list and the occurences of words after prefixes,
    and compare values

    Args:
        text_as_wordlist : A list of strings
        prefixes_in_sentences : Dictionary produced by method
                                get_occurences_for_number_of_sentences(
        printout : String. If "Full", occurences are printed to stdout

    Returns:
        Float. Average difference between occurences of words after
        prefixes in sentences, compared to occyrences in full text
    """
    i = 0
    sum_of_differences = 0.0
    for prefix, sentence_dict in prefixes_in_sentences.items():

        full_text_dict = get_following_word_occurences(text_as_wordlist, prefix)
        
        sentence_sum = total_occurences(sentence_dict)
        full_text_sum = total_occurences(full_text_dict)
        
        for word, num in sentence_dict.items():
            i += 1
            sentence_ratio = num/sentence_sum
            full_text_ratio = full_text_dict[word]/full_text_sum
            difference = abs(full_text_ratio - sentence_ratio)
            sum_of_differences += difference

            if printout == "Full":
                prefix_as_string = ' '.join(prefix) 
                print(f"Prefix: '{prefix_as_string:50}' Followed by: ", end='')
                print(f"  '{word:12}': Sentences: {sentence_ratio:3.1%} ", end='')
                print(f"  Full text: {full_text_ratio:3.1%}", end='')
                print(f" Diffence: {difference:2.3}")

    average_difference = sum_of_differences / i
    if printout == "Full":
        print(f"     Average: {average_difference:2.3%}")

    return average_difference

                
def get_following_word_occurences(wordlist, prefix):
    """Count the appearances of different words after given prefix

    Args:
        wordlist : List of strings
        prefix : List of strings

    Returns:
        Dictionary of strings (words) as keys and integers (occurences)
        as values.

    Example:
        Args:
            wordlist = ["aa", "bb", "cc", "bb", "dd", "aa", "bb", "cc", "aa", "bb", "aa"]
            prefix = ["aa", "bb"]
        Returns:
            {"cc" : 2, "aa": 1}
    """
    return_dict = {}

    prefix_length = len(prefix)

    for i in range(len(wordlist) - prefix_length):

        if wordlist[i:i+prefix_length] == list(prefix):  # prefix migth be list or tuple

            following_word = wordlist[i+prefix_length]
            if following_word in return_dict:
                return_dict[following_word] += 1
            else:
                return_dict[following_word] = 1

    return return_dict


def get_following_word_occurences_for_all_prefixes(wordlist, length):
    """Count the appearances of different words after given prefix

    Args:
        wordlist : List of strings
        length : Integer. Length of prefixes

    Returns:
        Dictionary of dictionaries, where keys are tuples of strings (prefixes)
        and values are dictionaries from get_following_word_occurences() method
        as values. The wordlist is split to length long pieces, and for each,
        the occurences of following words are counted

    Example:
        Args:
            wordlist = ["aa", "bb", "cc", "bb", "dd", "aa", "bb", "cc", "aa", "bb", "aa"]
            length = 3
        Returns:
            {("aa", "bb", "cc"): {"bb": 1, "aa": 1},
             ("bb", "cc", "bb"): {"dd": 1},
             ("cc", "bb", "dd"): {"aa": 1},
             ("bb", "dd", "aa"): {"bb": 1},
             ("dd", "aa", "bb"): {"cc": 1},
             ("bb", "cc", "aa"): {"bb": 1},
             ("cc", "aa", "bb"): {"aa": 1}}

    """
    return_dict = {}
    
    for i in range(len(wordlist) - length - 1):
        prefix = wordlist[i:i+length]

        prefix_as_tuple = tuple(prefix)
        
        if prefix_as_tuple not in return_dict:
            return_dict[prefix_as_tuple] = get_following_word_occurences(wordlist, prefix)

    return return_dict


def sum_occurences(first_dict, second_dict):
    """Combines word occurences in the dictionary. The first_dict
    is modified.

    Args:
        first_dict : Dictionary returned by get_following_word_occurences()
        second_dict : Dictionary returned by get_following_word_occurences()

    Example:
        first_dict = {"aa": 1}
        second_dict = {"aa": 1, "bb": 1}

        New value of first_dict: {"aa": 2, "bb": 1}
    """
    for word, occurences in second_dict.items():
        if word in first_dict:
            first_dict[word] += second_dict[word]
        else:
            first_dict[word] = second_dict[word]

            
def total_occurences(words):
    """Return sum of all following words occurences

    Args:
        words : Dictionary, where strings (words) are the keys, and
                their occurences the values

    Returns
        Integer

    Example:
        total_occurences({"aa": 2, "bb": 1, "cc": 3})
        returns 6
    """
    sum = 0

    for n in words.values():
        sum += n

    return sum


def sum_occurences_for_multiple_prefixes(first_dict, second_dict):
    """Combines word occurences in the dictionary for muliple prefixes.
    The first_dict is modified.

    Args:
        first_dict : Dictionary returned by get_following_word_occurences_for_all_prefixes()
        second_dict : Dictionary returned by get_following_word_occurences_for_all_prefixes()

    Example:
        first_dict = {("aa", "bb"): {"aa": 1, "bb":1}, ("bb", "cc"): {"aa": 1}}
        second_dict = {("aa", "bb"): {"bb":1}, ("bb", "dd"): {"aa": 1}}

        New value of first_dict:
        {("aa", "bb"): {"aa": 1, "bb":2}, ("bb", "cc"): {"aa": 1}, ("bb", "dd"): {"aa": 1}}
    """    
    for prefix, dict in second_dict.items():
        if prefix in first_dict:
            sum_occurences(first_dict[prefix], dict)
        else:
            first_dict[prefix] = dict

        
if __name__ == "__main__":

    print("Prefixes")
    wordlist = ["aa", "bb", "cc", "bb", "dd", "aa", "bb", "cc", "aa", "bb", "aa"]
    prefix = ["aa", "bb"]
    result = get_following_word_occurences(wordlist, prefix)
    print(result)
    result = get_following_word_occurences_for_all_prefixes(wordlist, 3)
    print(result)

    print("Sum dicts")
    first_dict = {"aa": 1}
    second_dict = {"aa": 1, "bb": 1}
    sum_occurences(first_dict, second_dict)
    print(first_dict)

    print("Sum all dicts")
    first_dict = {("aa", "bb"): {"aa": 1, "bb":1}, ("bb", "cc"): {"aa": 1}}
    second_dict = {("aa", "bb"): {"bb":1}, ("bb", "dd"): {"aa": 1}}
    sum_occurences_for_multiple_prefixes(first_dict, second_dict)
    print(first_dict)

    print("Should be 6:")
    print(total_occurences({"aa": 2, "bb": 1, "cc": 3}))
    
