class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Set = Counter(s1)


        l = 0
        r = len(s1)
        
        s2Set = Counter(s2[l:r])

        while r < len(s2):
            if s2Set == s1Set:
                return True
            s2Set[s2[l]] -= 1
            if s2Set[s2[l]] == 0:
                del s2Set[s2[l]]
            s2Set[s2[r]] += 1
            l += 1
            r += 1
        
        if s2Set == s1Set:
            return True
        
        return False

        