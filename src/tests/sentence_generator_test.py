import unittest

from sentence_generator import SentenceGenerator

class TestSentenceGenerator(unittest.TestCase):
    """ Test class for SentenceGenerator """
    def setUp(self):
        self.generator = SentenceGenerator(3)
        
        print("Setting up the test env for: SentenceGenerator")

    def test_empty_generator_has_correct_degree(self):
        self.assertEqual(self.generator.degree, 3)
        
    def test_empty_generator_has_correct_string_cast(self):
        self.assertEqual(str(self.generator), "DEG: 3 ROOT[0] ()")

    def tdest_empty_generator_reads_short_string_correctly(self):
        generator.read_string("aa bb")
        self.assertEqual(str(self.generator), "DEG: 3 ROOT[0] ('aa'[1] ('bb'[1] ())'bb[1] ()))")        
