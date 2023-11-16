# Laboratorium 3 Zadanie 3 Podpunkt 'a'

class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if (self.data == None):
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)

    def __str__(self, prefix="", is_left=True):
        result = ""
        if is_left:
            result += prefix + "`-- " + str(self.data) + "\n"
        else:
            result += prefix + "|-- " + str(self.data) + "\n"
        prefix += "    "
        if self.left:
            result += self.left.__str__(prefix, True)
        if self.right:
            result += self.right.__str__(prefix, False)
        return result

    @property
    def min_value(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.data

tree = Tree(5)
tree.insert(3)
tree.insert(7)
print(tree.min_value)