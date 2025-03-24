class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(i, result):
            if i == len(nums):
                results.append(result.copy())
                return
            
            result.append(nums[i])
            dfs(i + 1, result)
            
            result.pop()
            dfs(i + 1, result)

        dfs(0, [])
        return results