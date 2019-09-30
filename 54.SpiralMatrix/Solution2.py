class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    
        def runOneCircle(i, clen, rlen):
            res = []
            for j in range(0, clen):
                res.append(matrix[i][i+j])
            if rlen == 1:
                return res
            for j in range(1, rlen):
                res.append(matrix[i+j][i + clen -1])
            if clen == 1:
                return res
            for j in range(clen - 2, - 1, -1):
                res.append(matrix[i + rlen - 1][i + j])
            for j in range(rlen - 2, 0 , -1):
                res.append(matrix[i + j][i])
            print(res)
            return res
                
        res = []
        if not matrix:
            return res
        rlen = len(matrix)
        clen = len(matrix[0])
        res = runOneCircle( 0 , clen , rlen)
        rlen -= 2
        clen -= 2
        i = 1
        while( rlen > 0 and clen > 0):
            res += runOneCircle(i, clen, rlen)
            rlen -= 2
            clen -= 2
            i += 1
        return res