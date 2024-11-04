class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0,0

        while right < len(prices) :
            current_price = prices[right] - prices[left]
            if current_price > 0:
                max_profit = max(max_profit, current_price)
            else:
                left = right
            right += 1
        
        return max_profit
