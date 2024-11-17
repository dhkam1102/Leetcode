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