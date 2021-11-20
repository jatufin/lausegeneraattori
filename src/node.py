
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
        if token in self.children:
            return self.children[token]
        else:
            return None
        
    def add_token(self, new_token):
        if new_token not in self.children:
            self._new_child(new_token)
            
        self.children[new_token].weight_increment()
              
    def __str__(self):
        s = f"[{self.weight}] ("
        if self.has_children():
            for token, node in self.children.items():
                s += f"'{token}'" + str(node)
        s += ")"

        return s

    def _new_child(self, token):
        self.children[token] = Node()
    
def main():
    root = Node()
    #root.add_token("aa")
    #root.add_token("aa")

    print(root)


if __name__ == "__main__": main()
