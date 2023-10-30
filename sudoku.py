import tkinter as tk
from tkinter import ttk

def is_valid_move(grid, row, col, num):
    if num in grid[row] or num in [grid[i][col] for i in range(9)]:
        return False

    row_start, col_start = 3 * (row // 3), 3 * (col // 3)
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid_sudoku(grid):
    for i in range(9):
        row_set = set()
        col_set = set()
        for j in range(9):
            if grid[i][j] < 0 or grid[j][i] < 0 or grid[i][j] > 9:
                return False
            if grid[i][j] in row_set or grid[j][i] in col_set:
                return False
            if grid[i][j] != 0:
                row_set.add(grid[i][j])
            if grid[j][i] != 0:
                col_set.add(grid[j][i])

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid_set = set()
            for x in range(3):
                for y in range(3):
                    if grid[i + x][j + y] in subgrid_set:
                        return False
                    if grid[i + x][j + y] != 0:
                        subgrid_set.add(grid[i + x][j + y])

    return True

def solve_button_clicked():
    is_empty = all(entry.get() == '' for row in entries for entry in row)

    if is_empty:
        result_label.config(text="", foreground='black')
    else:
        for i in range(9):
            for j in range(9):
                entry = entries[i][j]
                if entry.get() == '':
                    sudoku_grid[i][j] = 0
                else:
                    sudoku_grid[i][j] = int(entry.get())

        if is_valid_sudoku(sudoku_grid):
            if solve_sudoku(sudoku_grid):
                for i in range(9):
                    for j in range(9):
                        entries[i][j].delete(0, tk.END)
                        entries[i][j].insert(0, str(sudoku_grid[i][j]))
                result_label.config(text="Sudoku Solved!", foreground='green')
            else:
                result_label.config(text="No solution found.", foreground='red')
        else:
            result_label.config(text="Sudoku is not valid.", foreground='red')

def check_button_clicked():
    is_empty = all(entry.get() == '' for row in entries for entry in row)

    if is_empty:
        result_label.config(text="", foreground='black')
    else:
        for i in range(9):
            for j in range(9):
                entry = entries[i][j]
                if entry.get() == '':
                    sudoku_grid[i][j] = 0
                else:
                    sudoku_grid[i][j] = int(entry.get())

        if is_valid_sudoku(sudoku_grid):
            result_label.config(text="Sudoku is valid.", foreground='green')
        else:
            result_label.config(text="Sudoku is not valid.", foreground='red')

def clear_button_clicked():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            sudoku_grid[i][j] = 0
    result_label.config(text="", foreground='black')

root = tk.Tk()
root.title("Sudoku Solver")

root.configure(bg='#E0E0E0')

# Create a frame for the heading with a colored background
heading_frame = ttk.Frame(root)
heading_frame.grid(row=0, column=0, columnspan=9, padx=10, pady=20, sticky="ew")
heading_frame.configure(style="Heading.TFrame")
style = ttk.Style()
style.configure("Heading.TFrame", background="#FFA500")  # Change the background color here

# Create a label for the heading within the frame
heading_label = tk.Label(heading_frame, text="Sudoku Solver", font=('Helvetica', 20, 'bold'), bg='#FFA500', fg='white')
heading_label.pack()

sudoku_frame = ttk.Frame(root)
sudoku_frame.grid(row=1, column=0, padx=10, pady=20, rowspan=9, columnspan=9)
sudoku_frame.configure(style="Light.TFrame")

style = ttk.Style()
style.configure("Light.TFrame", background="#FFFFFF")

style.configure("TButton", font=('Helvetica', 12))

entries = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        entry = tk.Entry(sudoku_frame, width=2, font=('Helvetica', 16), bd=1, relief="solid", bg='#F7F7F7', fg='black')
        entry.grid(row=i, column=j, padx=5, pady=5)
        entries[i][j] = entry

sudoku_grid = [[0 for _ in range(9)] for _ in range(9)]

button_frame = tk.Frame(root)
button_frame.grid(row=10, column=0, columnspan=9, padx=10, pady=20)

solve_button = tk.Button(button_frame, text="Solve Sudoku", command=solve_button_clicked, font=('Helvetica', 12), bg='#008000', fg='white')
solve_button.pack(side=tk.LEFT)

check_button = tk.Button(button_frame, text="Check", command=check_button_clicked, font=('Helvetica', 12), bg='#1E90FF', fg='white')
check_button.pack(side=tk.LEFT)

clear_button = tk.Button(button_frame, text="Clear", command=clear_button_clicked, font=('Helvetica', 12), bg='#FF4500', fg='white')
clear_button.pack(side=tk.LEFT)

result_label = tk.Label(root, text="", font=('Helvetica', 16), bg='#E0E0E0', fg='#008000')
result_label.grid(row=11, column=0, columnspan=9)

root.mainloop()
