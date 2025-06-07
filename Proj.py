lst_t = [
    [1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1]
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
    #Print input list:
    for r in lst:
        print(r)

    def find_way(row, col):
        nonlocal consist
        if row_len == row + 1 and lst[row][col] == 0:
            consist = True

        elif lst[row][col] == 0 and not checked[row][col]:
            checked[row][col] = True
            if col + 1 <= col_len - 1 and not checked[row][col + 1]:
                find_way(row, col + 1)
            if col - 1 >= 0 and not checked[row][col - 1]:
                find_way(row, col - 1)
            find_way(row + 1, col)

    for i in range(col_len):
        if lst[0][i] == 0:
            find_way(1, i)

    return consist


print(find_way_in_lst(lst_t))
