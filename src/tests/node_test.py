import unittest

from node import Node

class TestNode(unittest.TestCase):
    """ Test class for Node """

    def setUp(self):
        self.token_a = "aa"
        self.token_b = "bb"
        self.token_c = "cc"
        self.token_d = "dd"
        self.endchar = "."
        
        print("Setting up the test env for: Node")
        self.empty_root = Node()

        self.simple_tree = Node()
        self.simple_tree.add_token(self.token_a)
        self.simple_tree.add_token(self.token_a)
        self.simple_tree.add_token(self.token_b)

        self.long_tree = Node()
        self.token_list_a = [self.token_a, self.token_b, self.token_c]
        self.token_list_b = [self.token_b, self.token_b, self.token_c]        
        self.long_tree.add_token_list(self.token_list_a)
        self.long_tree.add_token_list(self.token_list_b)        


    def test_empty_root_str_cast_is_correct(self):
        self.assertEqual(
            str(self.empty_root),
            "[0] ()"
        )

    def test_empty_root_children_property_is_empty(self):
        self.assertEqual(
            self.empty_root.children,
            {}
        )

    def test_empty_root_has_no_children(self):
        self.assertFalse(
            self.empty_root.has_children()
        )

    def test_empty_root_returns_none_children(self):
        children = self.empty_root.get_children(self.token_a)
        self.assertEqual(
            children,
            None
        )
        
    def test_empty_root_add_token_works(self):
        self.empty_root.add_token(self.token_a)
        self.assertEqual(
            str(self.empty_root),
            f"[0] ('{self.token_a}'[1] ())"
        )

    def test_empty_root_add_token_list_works(self):
        token_list = [self.token_a, self.token_b, self.token_c]
        self.empty_root.add_token_list(token_list)
        self.assertEqual(
            str(self.empty_root),
            f"[0] ('{self.token_a}'[1] ('{self.token_b}'[1] ('{self.token_c}'[1] ())))"            
        )

    def test_empty_root_add_empty_token_list_doesnt_change_tree(self):
        tree_before = str(self.long_tree)
        self.long_tree.add_token_list([])
        tree_after = str(self.long_tree)
        self.assertEqual(tree_before, tree_after)
        
    def test_empty_root_add_two_equal_token_lists_works(self):
        token_list = [self.token_a, self.token_b, self.token_c]

        self.empty_root.add_token_list(token_list)
        self.empty_root.add_token_list(token_list)        

        self.empty_root.print_tree()
        
        self.assertEqual(
            str(self.empty_root),
            f"[0] ('{self.token_a}'[2] ('{self.token_b}'[2] ('{self.token_c}'[2] ())))"            
        )
        
    def test_empty_root_add_two_dissimilar_token_lists_works(self):
        token_list_1 = [self.token_a, self.token_b]
        token_list_2 = [self.token_b, self.token_c]        

        self.empty_root.add_token_list(token_list_1)
        self.empty_root.add_token_list(token_list_2)        

        self.empty_root.print_tree()
        
        self.assertEqual(
            str(self.empty_root),
            f"[0] ('{self.token_a}'[1] ('{self.token_b}'[1] ())'{self.token_b}'[1] ('{self.token_c}'[1] ()))"
        )
        
    def test_simple_tree_str_cast_is_correct(self):
        self.assertEqual(
            str(self.simple_tree),
            f"[0] ('{self.token_a}'[2] ()'{self.token_b}'[1] ())"
        )

    def test_simple_tree_token_count_increase_works(self):
        self.simple_tree.add_token(self.token_b)        
        self.assertEqual(
            str(self.simple_tree),
            f"[0] ('{self.token_a}'[2] ()'{self.token_b}'[2] ())"
        )

    def test_simple_tree_add_subtoken_works(self):        
        b = self.simple_tree.get_children(self.token_b)
        b.add_token(self.token_c)
        self.assertEqual(
            str(self.simple_tree),
            f"[0] ('{self.token_a}'[2] ()'{self.token_b}'[1] ('{self.token_c}'[1] ()))"
        )

    def test_children_total_weight_is_correct(self):
        total_weight = self.simple_tree._get_children_total_weight()
        self.assertEqual(total_weight, 3)

    def test_node_is_found_with_beginning(self):
        b = self.simple_tree.get_children(self.token_b)
        b.add_token(self.token_c)
        c = b.get_children(self.token_c)
        c.add_token(self.token_d)
        node = self.simple_tree._get_node_by_beginning([self.token_b, self.token_c])
        self.assertEqual(node.weight, 1)

    def test_node_is_not_found_with_false_beginning(self):
        b = self.simple_tree.get_children(self.token_b)
        b.add_token(self.token_c)
        c = b.get_children(self.token_c)
        c.add_token(self.token_d)
        node = self.simple_tree._get_node_by_beginning([self.token_a, self.token_c])
        self.assertEqual(node, None)

    def test_random_child_is_returned(self):
        a = ""
        b = ""
        none_returned = False
        
        # There are two childs on root, test if we get both of them with enough tries
        for i in range(20):
            random_word = self.simple_tree._get_random_child()
            if random_word == self.token_a:
                a = random_word
            if random_word == self.token_b:
                b = random_word
            if random_word == None: # A child should always be found
                none_returned = True

        self.assertEqual(a, self.token_a)
        self.assertEqual(b, self.token_b)
        self.assertFalse(none_returned)

    def test_no_random_child_is_returned_if_there_is_no_children(self):
        a = self.simple_tree.get_children(self.token_a)
        self.assertEqual(a._get_random_child(), None)

    def test_random_series_is_returned(self):
        list_a_found = False
        list_b_found = False
        none_returned = False
        
        for i in range(20):
            random_list = self.long_tree.get_random_series(3)
            if random_list == self.token_list_a:
                list_a_found = True
            if random_list == self.token_list_b:
                list_b_found = True
            if random_list == None:
                none_returned = True

        self.assertTrue(list_a_found)
        self.assertTrue(list_b_found)
        self.assertFalse(none_returned)
                
    def test_empty_random_series_is_returned_for_empty_tree(self):
        random_list = self.empty_root.get_random_series(3)
        self.assertEqual(random_list, [])

    def test_only_end_character_is_returned_in_random_series(self):
        tokenlist = [self.endchar, self.token_a]
        self.empty_root.add_token_list(tokenlist)
        randomlist = self.empty_root.get_random_series(2)
        self.assertEqual(randomlist, [self.endchar])

    def test_random_series_with_starting_words_works(self):
        starting_words = self.token_list_a[:2]
        found_words = self.long_tree.get_random_series_by_keywords(starting_words, 3)
        self.assertEqual(found_words, self.token_list_a)

    def test_random_series_with_empty_starting_words_returns_list(self):
        found_words = self.long_tree.get_random_series_by_keywords([], 3)
        self.assertGreater(len(found_words), 0)

    def test_random_series_with_too_many_starting_words_returns_none(self):
        starting_words = self.token_list_a * 2
        found_words = self.long_tree.get_random_series_by_keywords(starting_words, 3)
        self.assertIsNone(found_words)

    def test_random_series_with_invalid_starting_words_returns_none(self):
        starting_words = [self.token_d]
        found_words = self.long_tree.get_random_series_by_keywords(starting_words, 3)                
        self.assertIsNone(found_words)
