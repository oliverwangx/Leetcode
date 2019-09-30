class Solution:
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        def dfsHelper(x, y, index):
            if index == len(word): return True
            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board) or board[y][x] != word[index]:
                return False
            temp = board[y][x]
            board[y][x] = '$'
            res = dfsHelper(x, y+1, index+1) or dfsHelper(x, y-1, index+1) or \
                dfsHelper(x+1, y, index+1) or dfsHelper(x-1, y, index+1)
            board[y][x] = temp
            return res
                
        for y in range(len(board)):
            for x in range(len(board[0])):
                if dfsHelper(x, y, 0):
                    return True
        return False
a = Solution()
print(a.exist([["a","a"]],"aaa"))