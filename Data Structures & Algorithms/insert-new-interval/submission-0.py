class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        stack = []
        newStart, newEnd = newInterval

        for interval in intervals:

            if newEnd < interval[0]:
                stack.append(newInterval)
                newInterval = interval
            
            elif interval[1] < newStart:
                stack.append(interval)
            
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            
        stack.append(newInterval)
        
        return stack
        
        
            
            
            
            
            
        
        print(stack)