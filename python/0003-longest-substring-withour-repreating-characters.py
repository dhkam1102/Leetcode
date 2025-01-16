class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[r])
            result = max(r-l + 1, result)
        return result
