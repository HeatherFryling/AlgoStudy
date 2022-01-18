class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __repr__(self):
        return str([self.row, self.col])

# PURPOSE
# Given a chessboard with side length of n,
# find a placement of n queens such that none will
# attack each other.
# TIME COMPLEXITY
# O(n!) time. First choice: n rows. Second choice, n-1 rows...
# SPACE COMPLEXITY
# O(n) for the call stack and the path.
def n_queens(n):
    # Place one queen in each row.
    # Find the column for each row that doesn't conflict with others.
    solutions = []
    available_cols = set([i for i in range(n)])
    backtrack(n, 0, available_cols, set(), set(), [], solutions)
    return solutions

def backtrack(n, row, available_cols, used_diags, used_anti_diags, path, solutions):
    if len(path) == n:
        cp = path.copy()
        solutions.append(cp)
        return
    if row >= n:
        return
    for col in range(n):
        if col in available_cols:
            diag = row - col
            anti_diag = row + col
            if diag in used_diags or anti_diag in used_anti_diags:
                continue
            path.append(Cell(row, col))
            available_cols.remove(col)
            used_diags.add(diag)
            used_anti_diags.add(anti_diag)
            backtrack(n, row + 1, available_cols, used_diags, used_anti_diags, path, solutions)
            # Backtrack out
            path.pop()
            available_cols.add(col)
            used_diags.remove(diag)
            used_anti_diags.remove(anti_diag)
        # The last line only matters if the dimensions of the board can be greater than n.
        backtrack(n, row + 1, available_cols, used_diags, used_anti_diags, path, solutions)


c = Cell(0, 1)
print(c)
soln = n_queens(5)
for s in soln:
    print(s)
