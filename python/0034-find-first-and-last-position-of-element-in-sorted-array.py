class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findstart():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right)// 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid -1] != nums[mid]:
                        return mid
                    else:
                        right = mid -1
                elif nums[mid] > target:
                    right = mid -1
                else:         
                    left = mid + 1
            return -1

        def findend():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right)// 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != nums[mid]:
                        return mid
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                else:         
                    left = mid + 1
            return -1

    
        if not nums:
            return [-1, -1]

        start = findstart()
        if start == -1:
            return [-1, -1]
        
        end = findend()
        return [start, end]



    