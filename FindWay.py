import matplotlib.pyplot as plt

lst_t = [
    [1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1]
]
lst_t3 = [
    [1, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0]
]

lst_t2 = [
    [1, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 0]
]


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
                find_way(row, col + 1, lst_way)
            if col - 1 >= 0 and not checked[row][col - 1]:
                find_way(row, col - 1, lst_way)
            find_way(row + 1, col, lst_way)

    # find way in first row
    for i in range(col_len):
        if lst[0][i] == 0:
            find_way(1, i, lst_ways)
    for i_col in range(col_len):
        if lst_ways[1][i_col] and lst[0][i_col] == 0:
            lst_ways[0][i_col] = True

    return (True, lst_ways) if consist else (False,)


def create_matrix(lst_data, lst_ways):
    num_rows = len(lst_data)
    num_cols = len(lst_data[0])
    fig, ax = plt.subplots(figsize=(num_cols, num_rows))
    ax.axis("off")

    cell_colors = [['yellow' if cell else 'white' for cell in row] for row in lst_ways]

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


print("Welcome to this program\n"
      "This program shows the available paths to get from the first row to the last row.\n\n")

while True:
    selected_way = input("Please prees 1 for enter matrix from external file.\n"
                         "Please prees 2 for create random matrix.\n")
    if selected_way == '1' or selected_way == '2':
        selected_way = int(selected_way)
        break
    print("Please enter a valid number.")

solution = find_way_in_lst(lst_t3)
print("Way extant" if solution[0] else "no way")
create_matrix(lst_t3, find_way_in_lst(lst_t3)[1])
