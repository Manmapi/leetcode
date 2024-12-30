MOD = 1_000_000_007
class Solution:
    def numTilings(self, n: int) -> int:
        completed = [1]
        one = [0]
        two = [0]
        for i in range(1, n + 1):
            new_completed = completed[-1]
            if i >= 2:
                one.append(completed[-2] * 2 + one[-1])
                two.append(completed[-2])
                new_completed += two[-1]
                new_completed += one[-2]
            else:
                one.append(0)
                two.append(0)              
            completed.append(new_completed)
        return completed[-1] % MOD