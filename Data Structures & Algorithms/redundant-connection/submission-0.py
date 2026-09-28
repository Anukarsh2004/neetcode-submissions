class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        indegree = defaultdict(int)
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        
        q = deque()

        for node in indegree:
            if indegree[node] == 1:
                q.append(node)
        

        while q:
            node = q.popleft()
            indegree[node] -= 1

            for nei in adj[node]:
                indegree[nei] -=1
                if indegree[nei] == 1:
                    q.append(nei)
        
        for u,v in reversed(edges):
            if indegree[u] == 2 and indegree[v] == 2:
                return [u,v]
        
        return []


        