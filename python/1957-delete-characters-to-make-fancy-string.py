class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = ""
        count = 0
        result = ""
        for i in s:
            if i == prev and count > 2:
                continue
            elif i == prev and count < 2:
                count += 1
                result += i
            elif i != prev:
                prev = i
                count = 1
                result += i
        
        return result
