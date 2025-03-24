class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            current.append(candidates[i])
            total += candidates[i]
            dfs(i, current, total)

            current.pop()
            total -= candidates[i]
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return result