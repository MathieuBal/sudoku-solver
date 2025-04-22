# main.py
import tkinter as tk
from sudoku import create_grid, highlight_squares, solve_and_display, bind_navigation

def main():
    root = tk.Tk()
    root.title("Sudoku Solver")

    # 1) Création de la grille puis surlignage des blocs 3×3
    grid = create_grid(root)
    highlight_squares(grid)

    # 2) Bouton Résoudre
    solve_btn = tk.Button(root, text="Résoudre", command=lambda: solve_and_display(grid))
    solve_btn.grid(row=9, column=0, columnspan=9, pady=10)

    # 3) Navigation au clavier
    bind_navigation(grid)

    root.mainloop()

if __name__ == "__main__":
    main()
