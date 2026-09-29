class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        res = [[] for _ in range(n)]

        leftP = 1
        
        for i in range(n):
            res[i] = leftP
            leftP *= nums[i]
        

        rightP = 1
        for i in range(n-1,-1,-1):
            res[i] *= rightP
            rightP *= nums[i]
        
        return res
            
        