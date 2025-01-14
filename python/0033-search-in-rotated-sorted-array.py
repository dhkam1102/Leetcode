class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            #left portion of the array
            if nums[mid] >= nums[left]:
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[left]:
                    left = mid + 1
                else:
                    right = mid -1

            #right portion of the array
            else:
                if target > nums[right]:
                    right = mid - 1
                elif target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1

        return -1
                    
#여기서 중한건 그래프를 그려서 이해하기
# 항상 left, right portions of the graph and left will always be greater than right
# so first devided the portion and think