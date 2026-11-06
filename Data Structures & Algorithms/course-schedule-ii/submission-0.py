class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        ind = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for a,b in prerequisites:
            ind[a] += 1
            adj[b].append(a)
        

        q = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)

        
        order = []
        while q:
            crs = q.popleft()
            order.append(crs)

            for nxt in adj[crs]:
                ind[nxt] -= 1
                if ind[nxt] == 0:
                    q.append(nxt)
        

        for i in range(numCourses):
            if ind[i] != 0:
                return []
        

        return order
        