import unittest

from trie import TrieNode


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.token_a = "aa"
        self.token_b = "bb"
        self.token_c = "cc"
        self.token_d = "dd"

        self.empty_node = TrieNode()

        self.simple_tree = TrieNode(word=self.token_a)
        self.simple_tree._add_token(self.token_a)
        self.simple_tree._add_token(self.token_b)        

        self.long_tree = TrieNode()
        self.token_list_a = [self.token_a, self.token_b, self.token_c]
        self.token_list_b = [self.token_b, self.token_b, self.token_c]       
        self.long_tree.add_token_list(self.token_list_a)
        self.long_tree.add_token_list(self.token_list_b)
        
    def test_trienode_is_constructed(self):
        self.assertEqual(self.empty_node.word, "")        
        self.assertEqual(self.empty_node.weight, 0)
        self.assertEqual(self.empty_node.children, [])

    def test_has_children_tests_correctly_for_children(self):
        self.assertFalse(self.empty_node.has_children())
        self.assertTrue(self.simple_tree.has_children())

    def test_add_token_adds_word(self):
        self.empty_node._add_token("aa")
        self.assertTrue(self.empty_node.has_children())

    def test_add_token_increases_weight(self):
        self.empty_node._add_token("aa")
        self.empty_node._add_token("aa")
        self.assertTrue(self.empty_node._get_child("aa").weight, 2)
        
    def test_empty_node_add_token_works(self):
        self.empty_node._add_token(self.token_a)
        self.assertEqual(
            str(self.empty_node),
            f"''[0] ('{self.token_a}'[1] ())"
        )

    def test_empty_node_add_token_list_works(self):
        token_list = [self.token_a, self.token_b, self.token_c]
        self.empty_node.add_token_list(token_list)
        self.assertEqual(
            str(self.empty_node),
            f"''[0] ('{self.token_a}'[1] ('{self.token_b}'[1] ('{self.token_c}'[1] ())))"            
        )

    def test_empty_node_add_two_equal_token_lists_works(self):
        token_list = [self.token_a, self.token_b, self.token_c]

        self.empty_node.add_token_list(token_list)
        self.empty_node.add_token_list(token_list)        

        self.assertEqual(
            str(self.empty_node),
            f"''[0] ('{self.token_a}'[2] ('{self.token_b}'[2] ('{self.token_c}'[2] ())))"            
        )
        
    def test_empty_node_add_two_dissimilar_token_lists_works(self):
        token_list_1 = [self.token_a, self.token_b]
        token_list_2 = [self.token_b, self.token_c]        

        self.empty_node.add_token_list(token_list_1)
        self.empty_node.add_token_list(token_list_2)        

        self.assertEqual(
            str(self.empty_node),
            f"''[0] ('{self.token_a}'[1] ('{self.token_b}'[1] ())'{self.token_b}'[1] ('{self.token_c}'[1] ()))"
        )
        
    def test_addin_empty_token_list_adds_nothing(self):
        before = str(self.simple_tree)
        self.simple_tree.add_token_list([])
        after = str(self.simple_tree)
        self.assertEqual(before, after)

                
    def test_empty_random_series_is_returned_for_empty_tree(self):
        random_list = self.empty_node._get_random_series(3)
        self.assertEqual(random_list, [])
        
    def test_random_child_is_returned(self):
        a = ""
        b = ""
        none_returned = False
        
        # There are two childs on root, test if we get both of them with enough tries
        for i in range(20):
            random_word = self.simple_tree._get_random_child().word
            if random_word == self.token_a:
                a = random_word
            if random_word == self.token_b:
                b = random_word
            if random_word is None:  # A child should always be found
                none_returned = True

        self.assertEqual(a, self.token_a)
        self.assertEqual(b, self.token_b)
        self.assertFalse(none_returned)


    def test_random_series_is_returned(self):
        list_a_found = False
        list_b_found = False
        none_returned = False
        
        for i in range(20):
            random_list = self.long_tree._get_random_series(3)
            if random_list == self.token_list_a:
                list_a_found = True
            if random_list == self.token_list_b:
                list_b_found = True
            if random_list is None:
                none_returned = True

        self.assertTrue(list_a_found)
        self.assertTrue(list_b_found)
        self.assertFalse(none_returned)

    def test_random_series_with_starting_words_works(self):
        starting_words = self.token_list_a[:2]
        found_words = self.long_tree.get_random_series_by_keywords(
            starting_words, 3)
        self.assertEqual(found_words, self.token_list_a)

    def test_random_series_with_empty_starting_words_returns_list(self):
        found_words = self.long_tree.get_random_series_by_keywords([], 3)
        self.assertGreater(len(found_words), 0)

    def test_random_series_with_too_many_starting_words_returns_none(self):
        starting_words = self.token_list_a * 2
        found_words = self.long_tree.get_random_series_by_keywords(
            starting_words, 3)
        self.assertIsNone(found_words)

    def test_random_series_with_invalid_starting_words_returns_none(self):
        starting_words = [self.token_d]
        found_words = self.long_tree.get_random_series_by_keywords(
            starting_words, 3)
        self.assertIsNone(found_words)
