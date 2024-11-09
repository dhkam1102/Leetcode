class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = defaultdict(int)
        for i in s:
            hash_map[i] += 1

        for i in t:
            hash_map[i] -= 1
            # if hash_map[i] < 0:
            #     return False

        for i in hash_map:
            if hash_map[i] != 0:
                return False

        return True
