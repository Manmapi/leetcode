class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        rewards = [rewardValues[0]]
        for reward in rewardValues:
            if reward != rewards[-1]:
                rewards.append(reward)
        dp = 1 << 0
        for reward in rewards: 
            x = (dp & ((1 << reward) - 1)) << reward
            dp |= x
        return dp.bit_length() - 1