import random


class Node:
    """ Trie tree with weighted vertices """
    
    def __init__(self):
        """ Word itself is a key in dictionary object children, that why
        it's not property of the node itself
        """
        self.reset()

    def reset(self):
        self._weight = 0
        self._children = {}
        
    @property
    def weight(self):
        """ Weight is the number of occurences of a word after previous
        word in this branch of the tree. Node's weight in relation to total
        weight of it and its siblings, represents ndes probability to appear
        after the words above it in the tree
        """
        return self._weight

    @property
    def children(self):
        """ Dictionary of the words, which can follow the current node
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
    
    def get_child(self, token):
        """ Return a Node, if it can be found from the children dictionary,
        token is a string, i.e. word
        """
        if token in self.children:
            return self.children[token]
        else:
            return None

    def _get_children_total_weight(self):
        """ Sums up the weights of all the current nodes immediate children.
        This value is used, when probability of the next word appearing is
        added to the random select process
        """
        total = 0
        for word, node in self.children.items():
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
        if first_word in self.children:
            return self.children[first_word]._get_node_by_beginning(rest)
        return None

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
        for word, node in self.children.items():
            i += node.weight
            if i >= rnd:
                return word
        
    def get_random_series(self, depth):
        """ Get random depth length series of words from the tree
        """
        if depth == 0:
            return []
        word = self._get_random_child()
        if word is None:
            return []
        return [word] + self.children[word].get_random_series(depth-1)
        
    def is_valid_beginning(self, words):
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
            return self.get_random_series(depth)
        if number_of_words > depth:
            return None
        if not self.is_valid_beginning(words):
            return None
        starting_node = self._get_node_by_beginning(words)
        return words + starting_node.get_random_series(depth - number_of_words)

    def _new_child(self, token):
        """ Create new Node object and add it to the children of current node
        """
        self.children[token] = Node()
    
    def add_token(self, new_token):
        """ Add new token (word) to the children of the current. If it exists
        already, its weight is increased
        """
        if new_token not in self.children:
            self._new_child(new_token)
            
        self.children[new_token].weight_increment()

    def add_token_list(self, token_list):
        """ Add a sequence of tokens to the tree. If a token doesn't
            exist, it will be added
        """
        if not token_list:
            return

        # Recursive solution:
        # first_token = token_list[0]
        # rest = token_list[1:]
        # self.add_token(first_token)
        # if not self._is_end_character(first_token):
        #    self.get_child(first_token).add_token_list(rest)

        # Iterative solution:        
        current_node = self
        for token in token_list:
            current_node.add_token(token)
            current_node = current_node.get_child(token)
            
    def print_tree(self, indent=""):
        """ Print representation of the tree to stdout
        """
        print(":" + str(self.weight))
        for token, node in self.children.items():
            print(indent + str(token), end="")
            node.print_tree(indent + "  ")
            
    def __str__(self):
        """ String repesentation of te tree from current node downwards
        """
        s = f"[{self.weight}] ("
        for token, node in self.children.items():
            s += f"'{token}'" + str(node)
        s += ")"

        return s
