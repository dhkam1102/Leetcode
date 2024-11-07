#memoization
class Solution:
    def climbStairs(self, n: int, memo = None) -> int:
        if memo is None:
            memo = {}

        if n in memo:
            return memo[n]
        
        if n == 0:
            return 1

        if n < 0:
            return 0

        count = self.climbStairs(n -1, memo) + self.climbStairs(n - 2, memo)
        memo[n] = count

        return count
        