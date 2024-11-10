class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        item_dict = dict()
        n = len(items)
        for i in range(n):
            if items[i][0] not in item_dict or items[i][1] > item_dict[items[i][0]]:
                item_dict[items[i][0]] = items[i][1]
        items = [[k, v] for k, v in item_dict.items()]
        n = len(items)
        items.sort()
        new_items = [items[0]]
        for i in range(1, n):
            if items[i][1] > new_items[-1][1]:
                new_items.append([items[i][0], items[i][1]])
        items = new_items
        n = len(items)
        result = []
        for q in queries:
            l = 0
            r = n - 1
            flag = False
            while l <= r:
                mid = (l + r) // 2
                price, beauty = items[mid]
                if price > q: 
                    r = mid - 1
                else:
                    flag = True
                    l = mid + 1
            if not flag:
                result.append(0)
            else:
                result.append(items[r][1])
        return result