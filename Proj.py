lst_t = [
    [1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1],
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
    lst_ways = [[False for _ in range(col_len)] for _ in range(row_len)]

    # Print input list:
    for r in lst:
        print(r)

    def find_way(row, col, lst_way):
        nonlocal consist
        if True not in lst_way[0]:
            lst_way[0][col] = True
        if row_len == row + 1 and lst[row][col] == 0:
            lst_way[row][col] = True
            consist = True
            for way in lst_way:
                print(way)

        elif lst[row][col] == 0 and not checked[row][col]:
            checked[row][col] = True
            lst_way[row][col] = True
            if col + 1 <= col_len - 1 and not checked[row][col + 1]:
                find_way(row, col + 1, lst_way)
            if col - 1 >= 0 and not checked[row][col - 1]:
                find_way(row, col - 1, lst_way)
            find_way(row + 1, col, lst_way)

    for i in range(col_len):
        if lst[0][i] == 0:
            find_way(1, i, lst_ways)

    return "Yes, consist way" if consist else "no way"


print(find_way_in_lst(lst_t))
