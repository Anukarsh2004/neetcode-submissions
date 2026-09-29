class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        freq = [[] for _ in range (len(nums) + 1)]

        res = []

        for num, value in count.items():
            freq[value].append(num)  

        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
        