class PrefixTreeNode:
    def __init__(self):
        self.edges = dict()
        self.isTerminate = False


class PrefixTree:
    def __init__(self):
        self.head = PrefixTreeNode()

    def addWord(self, word):
        if len(word) == 0:
            return

        curNode = self.head
        for i in range(len(word)):
            if word[i] not in curNode.edges:
                curNode.edges[word[i]] = PrefixTreeNode()
            curNode = curNode.edges[word[i]]
        curNode.isTerminate = True

    def loadFromTxt(self, filename: str):
        pass

    def loadFromBin(self, filename: str):
        pass

    def saveToTxt(self, filename: str):
        pass

    def saveToBin(self, filename: str):
        pass
