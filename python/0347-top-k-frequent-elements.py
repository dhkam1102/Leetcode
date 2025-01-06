class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_dict = {}
        for i in nums:
            hash_dict[i] = hash_dict.get(i, 0) + 1

        max_heap = [[-freq, num] for num, freq in hash_dict.items()]
        heapq.heapify(max_heap)
        result = []
        for i in range(k):
            largest = heapq.heappop(max_heap)
            result.append(largest[1])

        return result
    
#using bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                

#time O(n)
#space O(n)