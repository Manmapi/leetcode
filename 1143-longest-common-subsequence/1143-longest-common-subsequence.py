class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        m = len(text1)
        n = len(text2)
        dp = [0] * (n + 1)
        for i in range(m):
            pre_val = 0
            for j in range(n):
                cur_val = dp[j + 1]
                if text1[i] == text2[j]:
                    dp[j + 1] = pre_val + 1
                else:
                    dp[j + 1] = max(dp[j], dp[j + 1]) 
                pre_val = cur_val
        return dp[-1]
                
