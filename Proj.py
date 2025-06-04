lst_t = [
    [1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1]
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

    def find_way(row, col):

        if row_len - 1 < row:
            print("row_len is less than row")
            return True

        if lst[row][col] == 0:
            find_way(row + 1, col)
            if col + 1 <= col_len - 1:
                find_way(row, col + 1)
            if col - 1 >= 0:
                find_way(row, col - 1)


    for i in range(col_len):
        if lst[0][i] == 0:
           if find_way(1, i):
               return True
    else:
        return False


print(find_way_in_lst(lst_t2))
