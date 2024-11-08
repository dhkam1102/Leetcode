class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(s):
            if not s:
                return True
            
            if s in memo:
                return memo[s]
            
            result = False
            for i in wordDict:
                if len(s) >= len(i) and s[:len(i)] == i:
                    if dfs(s[len(i):]):
                        result = True
                        break

            memo[s] = result
            return result

        result = dfs(s)
        return result
        

