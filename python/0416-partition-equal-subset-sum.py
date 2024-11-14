class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextdp = set()
            for t in dp:
                nextdp.add(t)
                nextdp.add(nums[i] + t)
            dp = nextdp
        
        if target in dp:
            return True
        else:
            return False