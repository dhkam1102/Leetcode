# my bruth force solution
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        
        return count
    
#solution using hash map and permutation
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        hash_map = Counter(nums)
        
        for k, v in hash_map.items():
            count += (v * (v - 1))//2

        return count
    
#using less math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        hash_map = defaultdict(int)

        for i in nums:
            if hash_map[i] == 0:
                hash_map[i] += 1
            else:
                count += hash_map[i]
                hash_map[i] += 1
        
        return count