import matplotlib.pyplot as plt
from copy import deepcopy
from random import randint
import pandas as pd
created_lst = []



def find_way_in_lst(lst):
    row_len = len(lst)
    col_len = len(lst[0])
    consist = False
    checked = [[False for _ in range(col_len)] for _ in range(row_len)]
    lst_ways = [[False for _ in range(col_len)] for _ in range(row_len)]

    def find_way(row, col, lst_way):
        nonlocal consist

        if row_len == row + 1 and lst[row][col] == 0:
            lst_way[row][col] = True
            consist = True
            nonlocal lst_ways
            lst_ways = lst_way

        elif lst[row][col] == 0 and not checked[row][col]:
            checked[row][col], lst_way[row][col] = True, True
            if col + 1 <= col_len - 1 and not checked[row][col + 1]:
                find_way(row, col + 1, deepcopy(lst_way))
            if col - 1 >= 0 and not checked[row][col - 1]:
                find_way(row, col - 1, deepcopy(lst_way))
            find_way(row + 1, col, deepcopy(lst_way))

    # find way in first row
    for i in range(col_len):
        if lst[0][i] == 0:
            find_way(1, i, deepcopy(lst_ways))

    for i_col in range(col_len):
        if lst_ways[1][i_col] and lst[0][i_col] == 0:
            lst_ways[0][i_col] = True

    return (True, lst_ways) if consist else (False,lst_ways)


def create_matrix(lst_data, lst_ways=None):
    num_rows = len(lst_data)
    num_cols = len(lst_data[0])
    fig, ax = plt.subplots(figsize=(num_cols, num_rows))
    ax.axis("off")

    if lst_ways is not None:
        cell_colors = [['yellow' if cell else 'white' for cell in row] for row in lst_ways]
    else:
        cell_colors = [['white' for _ in range(num_cols)] for _ in range(num_rows)]

    table = ax.table(
        cellText=lst_data,
        cellLoc='center',
        loc='center',
        cellColours=cell_colors,
    )
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1, 1)
    plt.show()


def read_matrix_from_excel(file_path, sheet_name=0):
    """
    Reads a 2D matrix from an Excel file

    Parameters:
        file_path (str): Path to Excel file
        sheet_name (str/int): Name or index of sheet (default: first sheet)

    Returns:
        list: 2D matrix (list of lists)
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

        matrix = df.values.tolist()

        return matrix

    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

print("Welcome to this program\n"
      "This program shows the available paths to get from the first row to the last row.\n\n")

while True:
    selected_way = input("Please prees 1 for enter matrix from external file.\n"
                         "Please prees 2 for create random matrix.\n")
    if selected_way == '1' or selected_way == '2':
        break
    print("Please enter a valid number.")

if selected_way == '1':
    pass
elif selected_way == '2':
    def get_number(statement):
        while True:
            num = input(statement)
            if num.isnumeric():
                return int(num)


    mat_rows = get_number("Please enter number of matrix rows: ")
    mat_columns = get_number("Please enter number of matrix columns: ")
    created_lst = [[randint(0, 1) for _ in range(mat_columns)] for _ in range(mat_rows)]


result = find_way_in_lst(created_lst)
if result[0]:
    create_matrix(created_lst, result[1])
else:
    print("no way")
    create_matrix(created_lst, result[1])


