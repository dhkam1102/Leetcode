#using memory
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [-1, -1]

        counter = Counter(nums)
        for i in range(1, len(nums) + 1):
            if counter[i] == 2:
                result[0] = i
            if counter[i] == 0:
                result[1] = i
        
        return result

#not using memory
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [-1, -1]

        for i in nums:
            i = abs(i)
            if nums[i - 1] < 0:
                result[0] = i
            nums[i - 1] = - nums[i - 1]

        for i, v in enumerate(nums):
            if v > 0 and i + 1 != result[0]:
                result[1] = i + 1
        return result