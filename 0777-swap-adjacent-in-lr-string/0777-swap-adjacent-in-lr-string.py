class Solution:
    def canTransform(self, start: str, target: str) -> bool:
        if start.replace("X", "") != target.replace("X", ""):
            return False
        i = l = r = 0
        n = len(start)
        while i < n:
            if start[i] == "R":
                r += 1
            if target[i] == "L":
                l += 1
            if start[i] == "L":
                if l <= 0:
                    return False
                else:
                    l -= 1
            if target[i] == "R":
                if r <= 0:
                    return False
                else:
                    r -= 1
            i += 1
        return True 