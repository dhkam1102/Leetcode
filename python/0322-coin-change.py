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
    

#이런식으로 안면 버그남

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins