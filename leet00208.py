class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur_trie = self.trie
        for ch in word:
            if ch not in cur_trie:
                cur_trie[ch] = {}
            cur_trie = cur_trie[ch]
        cur_trie['#'] = None
                

    def search(self, word: str) -> bool:
        cur_trie = self.trie
        for ch in word:
            if ch not in cur_trie:
                return False
            cur_trie = cur_trie[ch]
        if '#' not in cur_trie:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        cur_trie = self.trie
        for ch in prefix:
            if ch not in cur_trie:
                return False
            cur_trie = cur_trie[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
