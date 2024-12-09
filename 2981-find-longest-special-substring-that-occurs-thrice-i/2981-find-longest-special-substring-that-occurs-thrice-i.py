class Solution:
    def maximumLength(self, s: str) -> int:
        curr = s[0]
        count = 1
        counter = dict()
        i = 1
        n = len(s)
        result = 0
        while i < n:
            while i < n and s[i] == curr[-1]:    
                count += 1
                i += 1
            if count > result:
                result = max(result, count - 2)
                counter[curr * count] = counter.get(curr * count, 0) + 1
                if count > 1:
                    counter[curr * (count - 1)] = counter.get(curr * (count - 1), 0) + 2
            if i == n:
                curr = None
                break
            curr = s[i]
            i += 1
            count = 1
        counter[curr] = counter.get(curr, 0) + 1
        values = [len(k) for k, v in counter.items() if v >= 3]
        values.append(result)
        result = max(values) 
        return result or -1