class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 , rob2 = 0, 0

        for i in nums:
            temp = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
    
        return max(do(nums[1:]), do(nums[:-1]), nums[0])