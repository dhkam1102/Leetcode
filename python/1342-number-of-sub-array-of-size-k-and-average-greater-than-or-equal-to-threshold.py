class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = sum(arr[:k])
        left = 0
        count = 0

        if current_sum // k >= threshold:
            count += 1
        
        for i in range(k, len(arr)):
            current_sum += arr[i]
            current_sum -= arr[left]
            left += 1
            
            if current_sum // k >= threshold:
                count += 1
        
        return count