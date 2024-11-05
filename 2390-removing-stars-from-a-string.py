class Solution:
    def removeStars(self, s: str) -> str:
        my_stack = []
        for i in s:
            if i == "*":
                my_stack.pop()
            else:
                my_stack.append(i)
        
        result = "".join(my_stack)
        return result