## This One should be the best Solution !
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []

        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m-1, 0, n-1
        while l < r and u < d:
            res.extend([matrix[u][i] for i in range(l,r)] )
            res.extend([matrix[i][r] for i in range(u, d)])
            res.extend([matrix[d][i] for i in range(r,l,-1)])
            res.extend([matrox[i][l] for i in range(d,u,-1)])
            u, d, l, r = u+1, d-1, l+1, r-1
        if l == r:
            res.extend([matrix[i][r] for i in range(u, d+1)])
        elif u == d:
            res.extend([matrix[u][i] for i in range(l,r+1)])
        return res