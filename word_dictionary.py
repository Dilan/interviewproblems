# https://leetcode.com/problems/add-and-search-word-data-structure-design/

# Design a Dictionary that supports insert new word and search
# search(word) can search a literal word or a regular expression string containing
# only letters a-z or .. A . means it can represent any one letter.

class WordDictionary(object):

    def __init__(self):
        self.children = {}  # mapping from character ==> Node
        self.value = None

    def addWord(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()
            node = node.children[char]
        node.value = word

    def search(self, word):
        nodes = [self]

        for char in word:
            if char == '.':
                for idx, n in enumerate(nodes[:]):
                    if (idx == 0):
                        nodes = []

                    nodes += n.children.values()
            else:
                idx = 0
                for i,node in enumerate(nodes[:]):
                    if char in node.children:
                        nodes[idx] = node.children[char]
                        idx += 1
                nodes = nodes[:idx]

            if len(nodes) == 0:
                return False

        for n in nodes:
            if n.value is not None:
                return True

        return False

if __name__ == '__main__':
    wd = WordDictionary()
    words = ["ran","rune","runner","runs","adds"]
    for word in words:
        wd.addWord(word)

    data = [
        ('....e.', True),
        ('.a.', True),
        ('.an', True),
        ('ran', True),
        ('ra.', True),
    ]

    for item in data:
        search, answer = item
        result = wd.search(search)

        print('Search [' + search + ']: ', result, 'vs', answer)
