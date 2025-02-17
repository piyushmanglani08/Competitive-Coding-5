# Time Complexity : O(N^(2))
# Space Complexity : O(3N) = O(N) Comes from the three arrays used for bit masking
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_check = [0] * 9 
        col_check = [0] * 9
        square_check = [0] * 9
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] != ".":
                    
                    if  1 << int(board[i][j]) & row_check[i]: 
                        return False
                    else:
                        row_check[i] |= 1 << int(board[i][j])

                    if  1 << int(board[i][j]) & col_check[j]:
                        return False
                    else:
                        col_check[j] |= 1 << int(board[i][j])

                    square_num = (i // 3) * 3 + j // 3 
                    if 1 << int(board[i][j]) & square_check[square_num]:
                        return False
                    else:
                        square_check[square_num] |= 1 << int(board[i][j])
        
        return True