class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_len = 0

        for i in range(len(s)):

            #odd case
            l, r = i,i
            while l >= 0 and r < len(s) and s[l] ==s[r]:
                if (r - l + 1) > result_len:
                    result = s[l:r+ 1]
                    result_len = r - l + 1
                l -= 1
                r += 1
            
            #even case
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_len:
                    result = s[l: r+ 1]
                    result_len = r - l + 1
                l -= 1
                r += 1
            
        return result