class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        hash_set = set()
        for right in range(len(nums)):
            if right - left > k:
                hash_set.remove(nums[left])
                left += 1
            if nums[right] in hash_set:
                return True
            hash_set.add(nums[right])

        return False

#using hash_dict
# time: O(N), #space: O(N)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_dict = {}

        for i, v in enumerate(nums):
            if v in hash_dict and abs(i - hash_dict[v]) <= k:
                return True
            hash_dict[v] = i
        return False