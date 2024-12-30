class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        def find_possible(spell):
            target = ceil(success / spell) 
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                value = potions[mid]
                if value >= target :
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        return [n - find_possible(spell) for spell in spells]                