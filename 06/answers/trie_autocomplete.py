class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None


def trie_autocomplete(words: list[str], prefix: str) -> list[str]:
    root = TrieNode()

    # Insert unique words into the Trie to avoid duplicates
    for w in set(words):
        curr = root
        for char in w:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
        curr.word = w

    # Traverse to the end of the given prefix
    curr = root
    for char in prefix:
        if char not in curr.children:
            return []
        curr = curr.children[char]

    # Collect all words in the subtree in alphabetical order using DFS
    result = []

    def dfs(node: TrieNode):
        if node.is_end:
            result.append(node.word)
        # Sort keys to ensure lexicographical order
        for char in sorted(node.children.keys()):
            dfs(node.children[char])

    dfs(curr)
    return result
