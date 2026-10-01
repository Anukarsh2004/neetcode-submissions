class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)

        stack = []
        for i in range (len(temperatures)):
            tmp = temperatures[i]
            while stack and stack[-1][0] < tmp:
                ptmp, pIdx = stack.pop()
                result[pIdx] = i - pIdx
            
            stack.append([tmp, i])
        
        return result