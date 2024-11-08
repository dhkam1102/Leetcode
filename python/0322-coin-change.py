class Solution:
    def coinChange(self, coins: List[int], amount: int, memo = None) -> int:
        # Initialize memo only on first call
        if memo is None:
            memo = {}
            # Handle the final -1 conversion at the top level
            result = self.coinChange(coins, amount, {})
            return -1 if result == float('inf') else result
            
        # Base cases
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        if amount in memo:
            return memo[amount]
            
        # Try each coin
        min_count = float('inf')
        for coin in coins:
            min_count = min(min_count, 1 + self.coinChange(coins, amount - coin, memo))
                
        memo[amount] = min_count
        return min_count