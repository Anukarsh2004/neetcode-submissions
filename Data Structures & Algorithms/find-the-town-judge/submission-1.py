class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trustedBy = defaultdict(int)
        trusts = defaultdict(int)

        for a,b in trust:
            trusts[a] += 1
            trustedBy[b] += 1
        
        print(trusts)
        print(trustedBy)
        
        for i in range(1,n+1):
            if i not in trusts and trustedBy[i] == n - 1:
                return i


        return -1
        
        