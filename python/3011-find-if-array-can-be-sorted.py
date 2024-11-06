class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        i = 0
        last_element = 0
        while i < len(nums):
            max_chain = nums[i]
            min_chain = nums[i]
            j = i + 1
            while j < len(nums) and nums[j].bit_count() == nums[i].bit_count():
                max_chain = max(nums[j], max_chain)
                min_chain = min(nums[j], min_chain)
                j += 1
            if last_element > min_chain:
                return False
            i, last_element = j, max_chain

        return True

