class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rows = []
        length = []
        curr = []
        count = 0
        for word in words:
            if count == 0:
                count +=  len(word)
                curr.append(word)
                continue
            if count + 1 + len(word) <= maxWidth:
                count += 1 + len(word)
                curr.append(word)
            else:
                rows.append(curr)
                length.append(count)
                curr = [word]
                count = len(word)
        rows.append(curr)
        length.append(count)
        result = []
        for i, r in enumerate(rows[:-1]):
            extra = maxWidth - length[i]
            if len(r) == 1:
                result.append(r[0] + " " * (maxWidth - len(r[0])))
                continue
            pad = extra // (len(r) - 1)
            res = ""
            n = len(r)
            for i in range(n - 1):
                res += r[i]
                if extra > pad * (n - i - 1):
                    res += " " * (pad + 2)
                    extra -= pad + 1
                else:
                    res += " " * (pad + 1)
                    extra -= pad 
            res += r[-1]
            result.append(res)
        res = ""
        for word in rows[-1]:
            res += word + " "
        res = res[:-1]
        res += " " * (maxWidth - len(res))
        result.append(res)
        return result
