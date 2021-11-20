
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

    def add_token_list(self, token_list):
        if not token_list:
            return
        first_token = token_list[0]
        rest = token_list[1:]
        self.add_token(first_token)
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
    
def main():
    root = Node()
    root.add_token("aa")
    root.add_token("aa")
    root.add_token("bb")    
    root.get_children("bb").add_token("cc")
    root.get_children("bb").add_token("dd")
    root.get_children("bb").add_token("ee")
    
    root.get_children("aa").add_token("cc")    
    root.get_children("bb").get_children("dd").add_token("ff")

    root.add_token("ff")
    
    root.print_tree()


if __name__ == "__main__": main()
