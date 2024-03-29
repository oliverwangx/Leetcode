class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res = [[0] * n for _ in range(0,n)]
        u, d, l, r = 0, n-1, 0, n-1
        count = 1
        while (l < r and u < d):
            for i in range(l, r):
                res[u][i] = count
                count += 1
            for i in range(u, d):
                res[i][r] = count
                count += 1
            for i in range(r, l, -1):
                res[d][i] = count
                count += 1
            for i in range(d, u, -1):
                res[i][l] = count
                count += 1
            u, d, l, r = u+1, d-1, l+1, r-1
        if l == r:
            for i in range(u,d+1):
                res[i][l] = count
                count += 1
        elif u == d:
            for i in range(l, r+1):
                res[u][i] = count
                count += 1
        return res