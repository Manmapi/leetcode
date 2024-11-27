class Solution:
    def numWays(self, s: str) -> int:
        one_count = s.count("1")
        n = len(s)
        if one_count % 3:
            return 0
        if one_count == 0:
            return int((n - 1) * (n - 2) // 2) % 1_000_000_007
        per_chunk = one_count // 3
        chunks = []
        flag = False
        count = 0 
        for i in range(n):
            if s[i] == "1":
                if flag:
                    chunks.append(i)
                    flag = False
                    count = 1
                    if count == per_chunk:
                        chunks.append(i)
                        flag = True
                else:
                    count += 1
                    if count == per_chunk:
                        chunks.append(i)
                        flag = True
        return ((chunks[1] - chunks[0]) * (chunks[3] - chunks[2]) ) % 1_000_000_007
                
