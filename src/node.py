import random

class Node:
    """ Trie tree with weighted vertices """
    
    def __init__(self):
        self._weight = 0
        self._children = {}

    @property
    def weight(self):
        return self._weight

    def weight_increment(self):
        self._weight += 1

    @property
    def children(self):
        return self._children
    
    def has_children(self):
        return bool(self._children)

    def get_children(self, token):
        """ Return a Node, if it can be found from the children list """
        if token in self.children:
            return self.children[token]
        else:
            return None

    def _get_children_total_weight(self):
        total = 0
        for word, node in self.children.items():
            total += node.weight
        return total

    def _get_node_by_beginning(self, words):
        if words == []:
            return self
        first_word = words[0]
        rest = words[1:]
        if first_word in self.children:
            return self.children[first_word]._get_node_by_beginning(rest)
        return None

    def _get_random_child(self):
        total_weight = self._get_children_total_weight()
        rnd = random.randint(1, total_weight)

        i=0
        for word, node in self.children.items():
            i += node.weight
            if i >= rnd: return word
        
    def get_random_series(self, depth):
        ''' Get random depth length series of words from the tree '''
        if depth == 0:
            return []
        word = self._get_random_child()
        if self._is_end_character(word):
            return [word]
        return [word] + self.children[word].get_random_series(depth-1)

    def get_random_series_by_keywords(self, words, depth):
        ''' Follow first keywords, and after them random path
        returned list is depth long
        '''
        number_of_words = len(words)
        if number_of_words == 0:
            return self.get_random_series(self, depth)
        if number_of_words > depth:
            return None
        if not self.is_valid_beginning(words):
            return None
        starting_node = self._get_node_by_beginning(words)
        return words + starting_node.get_random_series(depth - number_of_words)
        
    def is_valid_beginning(self, words):
        return True if self._get_node_by_beginning(words) else False
    
    def add_token(self, new_token):
        if new_token not in self.children:
            self._new_child(new_token)
            
        self.children[new_token].weight_increment()

    def add_token_list(self, token_list):
        """ Add a sequence of tokens to the tree. If a token doesn't
            exist, it will be added """
        if not token_list:
            return
        first_token = token_list[0]
        rest = token_list[1:]
        self.add_token(first_token)

        if not self._is_end_character(first_token):
            self.get_children(first_token).add_token_list(rest)
            
    def print_tree(self, indent=""):
        print(":" + str(self.weight))
        for token, node in self.children.items():
            print(indent + str(token), end="")
            node.print_tree(indent + "  ")
            
    def __str__(self):
        s = f"[{self.weight}] ("
        for token, node in self.children.items():
            s += f"'{token}'" + str(node)
        s += ")"

        return s

    def _new_child(self, token):
        self.children[token] = Node()

    def _is_end_character(self, s):
        return s == "." or s == "!" or s == "?"

def main():
    pass

if __name__ == "__main__": main()
