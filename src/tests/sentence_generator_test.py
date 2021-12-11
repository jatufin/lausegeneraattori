import io
import sys
import unittest

from node import Node

from sentence_generator import SentenceGenerator
from sentence_generator import main as sg_main


class TestSentenceGenerator(unittest.TestCase):
    """ Test class for SentenceGenerator """
    def setUp(self):
        tree = Node()
        self.sg = SentenceGenerator(tree, 3)
        self.testfile_short = "src/tests/test_short.txt"
        self.testfile = "src/tests/test.txt"
        
    def test_empty_generator_has_correct_max_degree(self):
        self.assertEqual(self.sg.max_degree, 3)
        
    def test_empty_generator_has_correct_string_cast(self):
        self.assertEqual(str(self.sg), "DEG: 3 ROOT[0] ()")

    def test_empty_generator_reads_short_string_correctly(self):
        self.sg.read_string("aa bb")
        self.assertEqual(str(self.sg), "DEG: 3 ROOT[0] ('aa'[1] ('bb'[1] ())'bb'[1] ())")

    def test_reading_text_file_works(self):
        result = self.sg.read_file(self.testfile_short)
        self.assertTrue(result)
        self.assertEqual(str(self.sg), "DEG: 3 ROOT[0] ('aa'[1] ('bb'[1] ())'bb'[1] ())")

    def test_opening_nonexistent_file_fails(self):
        result = self.sg.read_file(self.testfile_short + "XXX")
        self.assertFalse(result)

    def test_number_of_words_in_string_counts_correctly(self):
        self.assertEqual(self.sg.number_of_words_in_string("aa bb cc"), 3)


    def test_number_of_different_words_in_string_counts_correctly(self):
        self.assertEqual(self.sg.number_of_different_words_in_string("aa bb bb cc"), 3)
        
        
        
    def test_printing_tree_works(self):
        capture = io.StringIO()
        sys.stdout = capture
        self.sg.print_tree()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture.getvalue(), ":0\n")

    def test_insert_token_list_works(self):
        self.sg._insert_token_list(["aa"])
        self.assertEqual(str(self.sg), "DEG: 3 ROOT[0] ('aa'[1] ())")

    def test_insert_empty_token_list_changes_nothing(self):
        before = str(self.sg)
        self.sg._insert_token_list([])
        after = str(self.sg)
        self.assertEqual(before, after)

    def test_get_sentence_as_list_returns_nonempty_list(self):
        self.sg.read_file(self.testfile)
        for i in range(10):
            wordlist = self.sg._get_sentence_as_list(degree=2, length=5, keywords=["aa"])
            self.assertGreater(len(wordlist), 0)

    def test_get_sentence_as_list_returns_empty_list_from_empty_tree(self):
        for i in range(10):
            wordlist = self.sg._get_sentence_as_list(degree=2, length=5, keywords=[])
            self.assertEqual(len(wordlist), 0)        

    def test_get_sentence_returns_nonempty_string(self):
        self.sg.read_file(self.testfile)
        for i in range(10):
            sentence = self.sg.get_sentence(degree=2, length=5, keywords=["aa"])
            self.assertGreater(len(sentence), 0)        

    def test_get_sentence_returns_empty_string_from_empty_tree(self):
        for i in range(10):
            sentence = self.sg.get_sentence(degree=2, length=5, keywords=["aa"])
            self.assertEqual(len(sentence), 0)        

    def test_get_sentence_as_list_returns_list_when_given_beginning(self):
        self.sg.read_string("aa bb")
        wordlist = self.sg._get_sentence_as_list(degree=2, length=5, keywords=["aa", "bb"])
        self.assertNotEqual(wordlist, [])
        
    def test_degree_value_validation_works(self):
        self.assertFalse(self.sg.is_degree_valid(0))
        self.assertFalse(self.sg.is_degree_valid(self.sg.max_degree + 1))
        self.assertTrue(self.sg.is_degree_valid(1))
        self.assertTrue(self.sg.is_degree_valid(self.sg.max_degree))

    def test_degree_string_value_validation_works(self):
        self.assertFalse(self.sg.is_string_valid_degree("1.0"))
        self.assertFalse(self.sg.is_string_valid_degree("F"))
        self.assertFalse(self.sg.is_string_valid_degree("0"))        
        self.assertTrue(self.sg.is_string_valid_degree("1"))

    def test_length_validation_returns_true_if_positive(self):
        self.assertTrue(self.sg.is_length_valid(1))

    def test_length_validation_returns_false_if_zero(self):
        self.assertFalse(self.sg.is_length_valid(0))        

    def test_length_validation_returns_false_if_negative(self):
        self.assertFalse(self.sg.is_length_valid(-1))

    def test_length_validation_returns_false_if_too_big(self):
        self.assertFalse(self.sg.is_length_valid(10000000))        

    def test_string_length_validation_for_number_works(self):
        self.assertTrue(self.sg.is_string_valid_length("1"))
        self.assertFalse(self.sg.is_string_valid_length("-1"))
        self.assertFalse(self.sg.is_string_valid_length("a"))
        self.assertFalse(self.sg.is_string_valid_length("10000000"))
        
    def test_main_without_argument_works(self):
        result = sg_main()
        self.assertEqual(result, 0)
