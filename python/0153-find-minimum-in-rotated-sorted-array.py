class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = nums[0]

        while left <= right:
            if nums[left] <= nums[right]:
                result = min(result, nums[left])
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return result
    

    #most important is that when rotated to find the minimum, 
    # nums[mid] >= nums[left]:
    # search the right portion of the array
    # since it will always contain the less unless the mid what the min