class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = collections.defaultdict(list)
        for i, dst in enumerate(edges):
            adj[i].append(dst)
        
        def bfs(src, distMap):
            q = deque()
            q.append([src, 0])
            distMap[src] = 0
            while q:
                node, dist = q.popleft()
                for neigh in adj[node]:
                    if neigh not in distMap:
                        q.append([neigh, dist + 1])
                        distMap[neigh] = dist + 1

        map1, map2 = {}, {}
        bfs(node1, map1)
        bfs(node2, map2)

        result = -1
        result_distance = float("inf")
        for i in range(len(edges)):
            if i in map1 and i in map2:
                distance = max(map1[i], map2[i])
                if distance < result_distance:
                    result = i
                    result_distance = distance
        return result