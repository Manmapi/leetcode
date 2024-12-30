class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        def find_possible(spell):
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                value = spell * potions[mid]
                if value >= success :
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        return [n - find_possible(spell) for spell in spells]                