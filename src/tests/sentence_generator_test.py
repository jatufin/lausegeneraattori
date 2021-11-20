import unittest

from sentence_generator import SentenceGenerator

class TestSentenceGenerator(unittest.TestCase):
    """ Test class for SentenceGenerator """
    def setUp(self):
        print("Setting up the test env")

    def test_foo(self):
        self.assertEqual("FOO", "FOO")

    def test_methods(self):
        s = "TESTSTRING"
        sg = SentenceGenerator()

        self.assertEqual(sg.readText(s), s)
        self.assertEqual(sg.save(s), s)
        self.assertEqual(sg.load(s), s)

        self.assertEqual(sg.generate(s), s)
        wordlist = ["aa", "bb"]
        self.assertEqual(sg.generate(s, wordlist), s + " aa bb")  
