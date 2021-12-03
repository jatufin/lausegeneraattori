import random

class TrieNode:
    def __init__(self, word="", weight=0):
        self._word = word
        self._weight = weight
        self._children = []

    @property
    def weight(self):
        """ Weight is the number of occurences of a word after previous
        word in this branch of the tree. Node's weight in relation to total
        weight of it and its siblings, represents ndes probability to appear
        after the words above it in the tree
        """
        return self._weight

    @property
    def word(self):
        return self._word

    @property
    def children(self):
        """ List of the node (words), which can follow the current node (word)
        """
        return self._children
    
    def weight_increment(self):
        """ When a node (word) is added to the tree, its weight is increased
        """
        self._weight += 1

    def has_children(self):
        """ Returns True, if the current node has children nodes at all
        """
        return bool(self._children)
        
    def _get_child(self, word):
        """ Returns a children node, if it is same word as the word given
        in the argument
        """
        for node in self._children:
            if node.word == word:
                return node

    def _get_children_total_weight(self):
        """ Sums up the weights of all the current nodes immediate children.
        This value is used, when probability of the next word appearing is
        added to the random select process
        """
        total = 0
        for node in self._children:
            total += node.weight
        return total

    def _get_node_by_beginning(self, words):
        """ Follow the list of words given in the tree, and return the last
        node. If the words of the list don't appear in the same order in
        the tree, None is returned.
        """
        if words == []:
            return self
        first_word = words[0]
        rest = words[1:]
        next_node = self._get_child(first_word)
        if not next_node:
            return None
        return next_node._get_node_by_beginning(rest)

    def _get_random_child(self):
        """ Select random word following current by adjusting randomness by the
        weights of the child nodes. If we have 3 childs, with weights 1,2
        and 3, the last one will be selected half the time
        """
        total_weight = self._get_children_total_weight()
        if total_weight == 0:
            return None
        
        rnd = random.randint(1, total_weight)

        i = 0
        for node in self.children:
            i += node.weight
            if i >= rnd:
                return node
    
    def _get_random_series(self, depth):
        """ Get random depth length series of words from the tree
        """
        if depth == 0:
            return []
        node = self._get_random_child()
        if node is None:
            return []
        return [node.word] + node._get_random_series(depth-1)
        
    def _is_valid_beginning(self, words):
        """ Gets list of words and evaluates, if there exists identical
        path downward from current node
        """
        return True if self._get_node_by_beginning(words) else False
    
    def get_random_series_by_keywords(self, words, depth):
        """ Follow first keywords, and after them random path until 
        depth words have been found
        """
        number_of_words = len(words)

        if number_of_words == 0:
            return self._get_random_series(depth)
        if number_of_words > depth:
            return None
        if not self._is_valid_beginning(words):
            return None
        starting_node = self._get_node_by_beginning(words)
        return words + starting_node._get_random_series(depth - number_of_words)

    def _new_child(self, word):
        """ Create new Node object and add it to the children of current node
        """
        self._children.append(TrieNode(word))
    
    def _add_token(self, new_word):
        """ Add new token (word) to the children of the current. If it exists
        already, its weight is increased
        """
        child_node = self._get_child(new_word)
        if not child_node:
            self._new_child(new_word)
            child_node = self._get_child(new_word)
         
        child_node.weight_increment()

    def add_token_list(self, token_list):
        """ Add a sequence of tokens to the tree. If a token doesn't
            exist, it will be added
        """
        if not token_list:
            return

        current_node = self
        for token in token_list:
            current_node._add_token(token)
            current_node = current_node._get_child(token)
        
    def print_tree(self, indent=""):
        """ Print representation of the tree to stdout
        """
        print(":" + str(self.weight))
        for node in self.children:
            print(indent + str(node.word), end="")
            node.print_tree(indent + "  ")
    
    def __str__(self):
        """ String repesentation of te tree from current node downwards
        """
        s = f"'{self.word}'[{self.weight}] ("
        for node in self.children:
            s += str(node)
        s += ")"

        return s
                    
class Trie:
    def __init__(self):
        self._root = TrieNode()

    def get_random_series_by_keywords(self, words, depth):
        """ Follow first keywords, and after them random path until 
        depth words have been found
        """
        return self._root.get_random_series_by_keywords(words, depth)

    def print_tree(self, indent=""):
        """ Print representation of the tree to stdout
        """
        self._root.print_tree()

    def add_token_list(self, token_list):
        """ Add a sequence of tokens to the tree. If a token doesn't
            exist, it will be added
        """
        self._root.add_token_list(token_list)

    def __str__(self):
        return str(self._root)
