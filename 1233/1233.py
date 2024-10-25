# Create a node for the trie so that we can determine if a level is terminal.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminate = False

# A trie class to insert all directories and remove the subfolders.
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # A level is marked as "terminate" if it the last in a given path.
    def add(self, seq: List[str]) -> None:
        cur = self.root

        for s in seq:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        cur.terminate = True

    # Explore with DFS until a terminal level, then write to an in-scope list.
    def remove(self) -> List[str]:
        scope_list = []

        def dfs(t: str, node: TrieNode) -> None:
            if node.terminate == True:
                scope_list.append(t)
                return
            for child in node.children:
                dfs(t + "/" + child, node.children[child])
        
        dfs("", self.root)
        return scope_list

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        # Add every directory to the trie, creating a new level for each folder.
        for f in folder:
            trie.add(f.split("/")[1:])
        
        return trie.remove()