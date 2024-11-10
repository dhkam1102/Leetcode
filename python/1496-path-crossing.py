class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0,0)}
        current = (0,0)

        for i in path:
            if i == "N":
                current = (current[0], current[1] + 1)
            elif i == "S":
                current = (current[0], current[1] - 1)
            elif i == "E":
                current = (current[0] + 1, current[1])
            elif i == "W":
                current = (current[0] - 1, current[1])

            if current in visited:
                return True

            visited.add(current)
        return False