class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        length1, length2 = len(str1), len(str2)

        def divisible(l):
            if length1 % l or length2 % l:
                return False
            
            f1 = length1 // l
            f2 = length2 // l

            if str1 == str1[:l] * f1 and str2 == str1[:l] * f2:
                return True

        for i in range(min(length1, length2), 0, -1):
            if divisible(i):
                return str1[:i]
        
        return ""

