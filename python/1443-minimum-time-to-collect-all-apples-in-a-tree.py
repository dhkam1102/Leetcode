class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = { i:[] for i in range(n)}

        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)

        def dfs(current, parent):
            time = 0

            for child in adj[current]:
                if child == parent:
                    continue

                child_time = dfs(child, current)
                if child_time or hasApple[child]:
                    time += child_time + 2
            
            return time
        
        return dfs(0, -1)