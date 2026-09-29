class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == ".":
                    continue
                
                if char in rows[r] or char in cols[c] or char in boxes[(r//3, c// 3)]:
                    return False
                
                rows[r].add(char)
                cols[c].add(char)
                boxes[(r//3,c//3)].add(char)
        
        return True
                
        