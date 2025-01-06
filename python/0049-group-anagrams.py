class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for string in strs:
            alpha_count = [0] * 26
            for c in string:
                alpha_count[ord(c) - ord("a")] += 1
            hash_map[tuple(alpha_count)].append(string)
        
        return list(hash_map.values())
    
# time O(m * n) m: number of words n: length of longest string
# space: O(m * n)