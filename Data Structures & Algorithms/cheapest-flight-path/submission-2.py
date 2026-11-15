class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        possible_flights = defaultdict(list)

        for frm,to,price in flights:
            possible_flights[frm].append((to,price))
        
       

        memo = {}
        
        def dfs(curr, stops):
            if stops > k+1:
                return float("inf")
            
            if curr == dst:
                return 0
            
            if (curr,stops) in memo:
                return memo[(curr,stops)]
            
            result = float("inf")
            for to,price in possible_flights[curr]:
                result = min (result, price + dfs(to, stops + 1))
            
            memo[(curr,stops)] = result
            

            return result
        
        result = dfs(src,0)
        
        return result if result != float('inf') else -1
        