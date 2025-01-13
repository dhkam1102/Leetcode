class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            else:
                stack.append([v, i])

        return result
