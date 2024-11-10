class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        items.sort()
        # Remove non-optimized items
        new_items = [items[0]]
        for i in range(1, n):
            if items[i][1] > new_items[-1][1]:
                new_items.append([items[i][0], items[i][1]])
        items = new_items
        n = len(items)
        @lru_cache(None)
        def bs(q):
            l = 0
            r = n - 1
            while l <= r:
                mid = (l + r) // 2 
                if items[mid][0] > q: 
                    r = mid - 1
                else:
                    l = mid + 1
            if r < 0 or l > n:
                return 0
            else:
                return items[r][1]
        
        result = []
        for q in queries:
            result.append(bs(q))
        return result