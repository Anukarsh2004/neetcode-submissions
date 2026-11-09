class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        seen = set()

        r = 0

        for l in range(len(nums)):
            if nums[l] in seen:
                while r < len(nums) and nums[r] in seen:
                    r += 1
                if r == len(nums):
                        break
                nums[l] = nums[r]
            seen.add(nums[l])
            r = max(r, l + 1)
           
            
        
        return len(seen)

        