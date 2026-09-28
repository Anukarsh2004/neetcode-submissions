class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        stack = []
        intervals.sort(key=lambda pair: pair[0])
        stack.append(intervals[0])
        for interval in intervals[1:]:
            if interval[0] > stack[-1][1]:
                stack.append(interval)
            
            else:
                start, end = stack.pop()
                stack.append([min(start,interval[0]), max(end,interval[1])])
        
        return stack

        