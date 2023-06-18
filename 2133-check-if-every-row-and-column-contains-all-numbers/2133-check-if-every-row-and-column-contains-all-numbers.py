class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        
        print(len(matrix))
        
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if(matrix[r][c] in rows[r] or matrix[r][c] in cols[c]):
                    return False
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
        return True