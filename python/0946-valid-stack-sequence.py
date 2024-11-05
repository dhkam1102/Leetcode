class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        my_stack = []
        j = 0
        for i in range(len(pushed)):
            my_stack.append(pushed[i])
            while j in range(len(popped)) and my_stack and popped[j] == my_stack[-1]:
                my_stack.pop()
                j += 1
        
        return False if my_stack else True