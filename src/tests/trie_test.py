import unittest

from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.token_a = "aa"
        self.token_b = "bb"
        self.token_c = "cc"
        self.token_d = "dd"

        self.empty_root = Trie()

        self.simple_tree = Trie()
        self.simple_tree.add_token_list([self.token_a])
        
    def test_empty_root_has_trie_node(self):
        self.assertIsNotNone(self.empty_root._root)

    def test_empty_root_str_cast_is_correct(self):
        self.assertEqual(
            str(self.empty_root),
            "''[0] ()"  # This differs from empty Node() tree, which is "[0] ()"
        )

    def test_get_random_series_by_keywords_returns_words(self):
        words = self.simple_tree.get_random_series_by_keywords(["aa"], 1)
        self.assertEqual(words, ["aa"])


    def test_add_token_list_adds_tokens(self):
        self.empty_root.add_token_list(["aa"])
        self.assertEqual(
            str(self.empty_root),
            f"''[0] ('{'aa'}'[1] ())"
        )

