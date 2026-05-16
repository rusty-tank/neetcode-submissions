from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # print(board)
        return self.ruleone(board) and self.ruletwo(board) and self.rulethree(board)
    
    def ruleone(self, board):
        for line in board:
            mapper = defaultdict(int)
            for c in line:
                if c != ".":
                    if mapper[c] == 0:
                        mapper[c] += 1
                    else:
                        return False
        return True
    
    def ruletwo(self, board):
        cols = []
        for i in range(len(board)):
            print(i)
            col = []
            for j in range(len(board)):
                col.append(board[j][i])
                # print(board[j][i])
            print(col)
            cols.append(col)
        
        for line in cols:
            mapper = defaultdict(int)
            for c in line:
                if c != ".":
                    if mapper[c] == 0:
                        mapper[c] += 1
                    else:
                        return False
        return True

    def rulethree(self, board):

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                mapper = defaultdict(int)

                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):

                        val = board[r][c]

                        if val != ".":

                            if mapper[val]:
                                return False

                            mapper[val] += 1

        return True