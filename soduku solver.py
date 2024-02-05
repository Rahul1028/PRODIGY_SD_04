import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")

        self.create_widgets()

    def create_widgets(self):
        self.entries = [[0]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.entries[i][j] = tk.Entry(self.master, width=2, font=("Helvetica", 16))
                self.entries[i][j].grid(row=i, column=j)
        
        self.solve_button = tk.Button(self.master, text="Solve Sudoku", command=self.solve_sudoku)
        self.solve_button.grid(row=9, column=4, pady=10)

    def solve_sudoku(self):
        board = self.get_board()
        if self.solve(board):
            self.display_solution(board)
        else:
            messagebox.showinfo("No Solution", "No solution exists for the given Sudoku puzzle.")

    def solve(self, board):
        empty_loc = self.find_empty_location(board)
        if not empty_loc:
            return True  # Puzzle solved

        row, col = empty_loc

        for num in range(1, 10):
            if self.is_valid(board, row, col, num):
                board[row][col] = num

                if self.solve(board):
                    return True

                board[row][col] = 0  # Undo the choice if it leads to a dead end

        return False

    def find_empty_location(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None

    def is_valid(self, board, row, col, num):
        # Check row
        if num in board[row]:
            return False

        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                entry_value = self.entries[i][j].get()
                if entry_value:
                    row.append(int(entry_value))
                else:
                    row.append(0)
            board.append(row)
        return board

    def display_solution(self, board):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, board[i][j])

def main():
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()

if __name__ == "__main__":
    main()
