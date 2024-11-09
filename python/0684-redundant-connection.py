class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #my dfs solution

        current_graph = defaultdict(list)

        def check_path(start, dest):
            if start == dest:
                return True
            
            visited.add(start)

            for neighbor in current_graph[start]:
                if neighbor not in visited:
                    if check_path(neighbor, dest):
                        return True
                
            return False
                    

        for start, dest in edges:
            visited = set()
            if check_path(start, dest):
                return [start, dest]
            
            else:
                current_graph[start].append(dest)
                current_graph[dest].append(start)
            
        return None
        