list = {
    "A": .02,
    "B": .03,
    "C": .04,
    "D": .06,
    "E": .07,
    "F": .08,
    "G": .09,
    "H": .11,
    "I": .20,
    "J": .30
}

class Node:
    def __init__(self, symbol, value, left=None, right=None):
        self.symbol = symbol
        self.value = value
        self.left = left
        self.right = right
        self.huff = ""

    def IsLeaf(self):
        return self.left is None and self.right is None

    def UpdateHuff(self):
        if not self.IsLeaf():
            self.left.huff = self.huff + "0"
            self.left.UpdateHuff()
            self.right.huff = self.huff + "1"
            self.right.UpdateHuff()
        
    def PrintHuff(self):
        if not self.IsLeaf():
            self.left.PrintHuff()
            self.right.PrintHuff()
        else:
            print(f"{self.symbol} -- {self.value} --> {self.huff}")


class HuffmanTree:
    def __init__(self):
        self.root = None
    
    def BuildTree(self, input):
        leafArray = []
        for key in input:
            leafNode = Node(key, input[key])
            leafArray.append(leafNode)
        
        while len(leafArray) > 1:
            leafArray.sort(key=lambda x: x.value, reverse=True)
            right = leafArray.pop()
            left = leafArray.pop()
            parentNode = Node(left.symbol + right.symbol, left.value + right.value, left, right)
            leafArray.append(parentNode)

        self.root = leafArray[0]

    def UpdateHuff(self):
        self.root.UpdateHuff()
    
    def PrintTable(self):
        self.root.PrintHuff()

tree = HuffmanTree()
tree.BuildTree(list)
tree.UpdateHuff()
tree.PrintTable()