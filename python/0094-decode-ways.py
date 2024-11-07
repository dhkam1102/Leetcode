#memoization approach
class Solution:
    def numDecodings(self, s: str, memo = None) -> int:
        if memo is None:
            memo = {}

        if s in memo:
            return memo[s]
        
        if not s:
            return 1
        
        if s[0] == "0":
            return 0
        
        count = self.numDecodings(s[1:], memo)
        
        if len(s) >= 2 and 10 <= int(s[:2]) <= 26:
            count += self.numDecodings(s[2:], memo)
        
        memo[s] = count
        return count
    
    