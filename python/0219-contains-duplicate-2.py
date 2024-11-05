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