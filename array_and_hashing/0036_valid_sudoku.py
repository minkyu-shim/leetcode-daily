# Level: medium
# Date: 2025-06-10

class Solution:
    def is_valid_sudoku(self, board):
        rows = {1 : set(), 2 : set(), 3 : set(), 4 : set(), 5 : set(), 6 : set(), 7 : set(),
                8 : set(), 9 : set()}
        columns = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(),
                8: set(), 9: set()}

        for i, row in enumerate(board):
            for j, el in enumerate(row):
                check = 0
                if el != "." and el not in rows[i]:
                    rows[i].add(el)
                if el in rows[i]:
                    return False