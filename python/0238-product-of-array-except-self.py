class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    #             [1,2,3,4]
    # prefix      [1,2,6,24]
    # post        [24,24,12,4]
    # output      [24, 12, 8, 6]

        pre = [0] * len(nums)
        suff = [0] * len(nums)
        result = [0] * len(nums)
        pre[0], suff[-1] = 1, 1

        for i in range(1, len(nums)):
            pre[i] = nums[i - 1] * pre[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        for i in range(len(nums)):
            result[i] = pre[i] * suff[i]

        return result