class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [[p,s] for p,s in zip(position, speed)]
        pairs.sort(reverse = True)
        stack = []

        for i in range(len(position)):
            time = (target - pairs[i][0]) / pairs[i][1]

            if stack and time <= stack[-1]:
                continue
            
            stack.append(time)


        return len(stack)
        