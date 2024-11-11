class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        # stats = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        stat_dict = defaultdict(dict)
        for i in range(n):
            stat_dict[endTime[i]][startTime[i]] = max(stat_dict[endTime[i]].get(startTime[i], 0), profit[i])
        # stats.sort(key=lambda x: (x[0], -x[2], x[1]))
        endTime.sort()
        max_dict = [[0, 0]]
        for end in endTime:
            max_profit = max(x for x in stat_dict[end].values())
            # print(end, max_dict[index - 1])
            # print("End: ", end)
            for start, profit in stat_dict[end].items():
                start_index = bisect.bisect_right(max_dict, start, key=lambda x: x[0]) - 1
                # print("Start:", start, max_dict[start_index])
                max_profit = max(profit + max_dict[start_index][1], max_profit)
            if max_profit > max_dict[-1][1]:
                max_dict.append([end, max_profit])
        return max_dict[-1][1]
