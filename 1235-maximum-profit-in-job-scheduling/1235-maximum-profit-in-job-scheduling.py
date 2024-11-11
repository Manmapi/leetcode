class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        stat_dict = defaultdict(dict)
        for i in range(n):
            stat_dict[endTime[i]][startTime[i]] = max(stat_dict[endTime[i]].get(startTime[i], 0), profit[i])
        endTime.sort()
        max_dict = [[0, 0]]
        for end in endTime:
            max_profit = max(x for x in stat_dict[end].values())
            for start, profit in stat_dict[end].items():
                start_index = bisect.bisect_right(max_dict, start, key=lambda x: x[0]) - 1
                max_profit = max(profit + max_dict[start_index][1], max_profit)
            if max_profit > max_dict[-1][1]:
                max_dict.append([end, max_profit])
        return max_dict[-1][1]
