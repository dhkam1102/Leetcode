class Solution:
    def coinChange(self, coins: List[int], amount: int, memo = None) -> int:
        if memo is None:
            memo = {}

        if amount in memo:
            return memo[amount]

        if amount < 0:
            return float("inf")
        
        if amount == 0:
            return 0

        min_count = float("inf")
        for i in coins:
            count = self.coinChange(coins, amount - i, memo)
            if count != float("inf"):  # Only add 1 if we found a valid solution
                min_count = min(min_count, count + 1)

        memo[amount] = min_count
        return min_count if min_count != float("inf") else -1