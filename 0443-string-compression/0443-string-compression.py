class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = [chars[0], 1]
        result = []
        i = 0
        for c in chars[1:]:
            if c == curr[0]:
                curr[1] += 1
            else:
                result.append(curr[0])
                if curr[1] > 1:
                    result.extend(str(curr[1]))
                curr = [c, 1]
        result.append(curr[0])
        if curr[1] > 1:
            result.extend(str(curr[1]))
        for i, r in enumerate(result):
            chars[i] = result[i]
        return len(result)