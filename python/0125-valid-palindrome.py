class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(c for c in s if c.isalnum())
        s = s.lower()

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True