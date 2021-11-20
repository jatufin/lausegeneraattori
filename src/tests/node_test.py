import unittest

from node import Node

class TestNode(unittest.TestCase):
    """ Test class for Node """

    def setUp(self):
        self.token_a = "aa"
        self.token_b = "bb"
        self.token_c = "cc"        
        
        print("Setting up the test env for: Node")
        self.empty_root = Node()

        self.simple_tree = Node()
        self.simple_tree.add_token(self.token_a)
        self.simple_tree.add_token(self.token_a)
        self.simple_tree.add_token(self.token_b)        

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


    
