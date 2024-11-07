class Trie:
    def __init__(self):
        self.child = {}
    
    def insert(self, value):
        curr = self.child
        value = value.split("/")[1:]
        for w in value:
            curr = curr.setdefault(w, {})
            if curr.get("endword"):
                return False

        curr["endword"] = True
        return True


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        result = []
        folder.sort(key=lambda x: len(x))
        for f in folder:
            flag = trie.insert(f)
            if flag:
                result.append(f)
        return result
        