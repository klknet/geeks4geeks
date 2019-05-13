"""
Pattern Searching using a trie of all suffices.
Following are steps to search a pattern in the build trie.
1)Starting from the first character of the pattern and the root of the trie, do following for every character.
...a)For the current character of the pattern, if there is an edge from the current node, follow the edge.
...b)If there is no edge, print "pattern doesn't exist in the text" and return
2)If all characters of pattern have been processed, i.e. if there is a path from root for the characters of the given
pattern, then print all indexes where pattern is present. To store indexes, we use a list with every node that stores
indexes of suffices starting at the node.
"""

no_of_chars = 256


class TrieNode(object):
    def __init__(self):
        self.children = [None] * no_of_chars
        self.index = []

    def insert_node(self, s, idx):
        self.index.append(idx)
        if len(s) == 0:
            return
        if self.children[ord(s[0])] is None:
            self.children[ord(s[0])] = TrieNode()
        self.children[ord(s[0])].insert_node(s[1:], idx+1)

    def search(self, pat):
        if len(pat) == 0:
            return self.index
        if self.children[ord(pat[0])] is not None:
            return self.children[ord(pat[0])].search(pat[1:])
        else:
            return


class TrieTree(object):
    def __init__(self, txt):
        self.root = TrieNode()
        self.txt = txt

    def build_trie(self):
        for i in range(len(self.txt)):
            self.root.insert_node(self.txt[i:], i)

    def search(self, pat):
        indexes = self.root.search(pat)
        if indexes is not None:
            for i in indexes:
                print(i-len(pat), end=' ')
        else:
            print('not found')
        print()


txt = "geeksforgeeks.org"
trie = TrieTree(txt)
trie.build_trie()

pat = "ee"
print('search for pat', pat)
trie.search(pat)

pat = "geek"
print('search for pat', pat)
trie.search(pat)

pat = "quiz"
print('search for pat', pat)
trie.search(pat)

pat = "forgeeks"
print('search for pat', pat)
trie.search(pat)
