# This function only run once
def find_prime():
    # Find all primes < 1000
    non_primes = set([1])
    primes = set([2])
    for i in range(3, 1000, 2):
        if i in non_primes:
            continue
        else:
            primes.add(i)
            k = 2
            while k * i < 1000:
                non_primes.add(k * i)
                k += 1
    return primes
primes = find_prime()

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        curr = 0
        for num in nums:
            flag = False
            for i in range(num - curr - 1, -1, -1):
                if (i in primes or i == 0) and num - i > curr:
                    curr = num - i
                    flag = True
                    break
            if not flag:
                return False
        return True