class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        ind = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for a,b in prerequisites:
            ind[a] += 1
            adj[b].append(a)
        

        q = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)

        
        while q:
            crs = q.popleft()

            for nxt in adj[crs]:
                ind[nxt] -= 1
                if ind[nxt] == 0:
                    q.append(nxt)
        

        for i in range(numCourses):
            if ind[i] != 0:
                return False
        

        return True

        
