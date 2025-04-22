# sudoku.py
import tkinter as tk

def solve_sudoku(grid):
    def can_place(i, j, val):
        # lignes et colonnes
        if any(int(cell.get()) == val for cell in grid[i] if cell.get()):
            return False
        if any(int(grid[r][j].get()) == val for r in range(9) if grid[r][j].get()):
            return False
        # carré 3×3
        i0, j0 = (i//3)*3, (j//3)*3
        for di in range(3):
            for dj in range(3):
                cell = grid[i0+di][j0+dj]
                if cell.get() and int(cell.get()) == val:
                    return False
        return True

    def backtrack(i=0, j=0):
        if i == 9:
            return True
        ni, nj = (i, j+1) if j < 8 else (i+1, 0)
        if grid[i][j].get():
            return backtrack(ni, nj)
        for val in range(1, 10):
            if can_place(i, j, val):
                grid[i][j].delete(0, tk.END)
                grid[i][j].insert(0, str(val))
                if backtrack(ni, nj):
                    return True
                grid[i][j].delete(0, tk.END)
        return False

    backtrack()

def create_grid(root):
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            e = tk.Entry(root, width=2, justify='center')
            e.grid(row=i, column=j, padx=1, pady=1)
            row.append(e)
        grid.append(row)
    return grid

def highlight_squares(grid):
    blocs = [
        (0,0), (0,6), (3,3), (6,0), (6,6)
    ]
    for bi, bj in blocs:
        for di in range(3):
            for dj in range(3):
                grid[bi+di][bj+dj].configure(bg='lightyellow')

def solve_and_display(grid):
    # mémoriser la saisie initiale
    start = [[cell.get() for cell in row] for row in grid]
    solve_sudoku(grid)
    # mettre en rouge ce qui a été ajouté
    for i in range(9):
        for j in range(9):
            if not start[i][j]:
                grid[i][j].configure(fg='red')

def bind_navigation(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            cell.bind("<Left>",  lambda e, i=i, j=j: grid[i][j-1].focus_set() if j>0   else None)
            cell.bind("<Right>", lambda e, i=i, j=j: grid[i][j+1].focus_set() if j<8   else None)
            cell.bind("<Up>",    lambda e, i=i, j=j: grid[i-1][j].focus_set() if i>0   else None)
            cell.bind("<Down>",  lambda e, i=i, j=j: grid[i+1][j].focus_set() if i<8   else None)
