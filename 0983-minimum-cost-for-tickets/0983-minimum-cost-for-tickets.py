class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        @cache
        def dp(last, current):
            if current >= n:
                if last is None:
                    return 0
                else:
                    return float("inf")
            results = []
            new_last = last
            if last is None:
                results.append(min(costs) + dp(None, current + 1))
                results.append(dp(current, current + 1))
            else:
                if days[current] - days[last] < 7:
                    results.append(costs[1] + dp(None, current + 1))
                if days[current] - days[last] < 30:
                    results.append(costs[2] + dp(None, current + 1))
                # if days[current] - days[last] >= 30:
                #     return float("inf")
                results.append(dp(last, current + 1))
            result = min(results)
            return result
        return dp(None, 0)