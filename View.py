import sys, os, random
import openpyxl
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt
from copy import deepcopy
from random import randint


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

    return (True, lst_ways) if consist else (False, lst_ways)


def display_matrix(table, matrix, highlight=None):
    table.clear()
    table.setRowCount(len(matrix))
    table.setColumnCount(len(matrix[0]))
    table.horizontalHeader().hide()
    table.verticalHeader().hide()
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QFont("Tahoma", 12))
            if highlight and highlight[i][j]:
                item.setBackground(QColor("#a5d6a7"))
            table.setItem(i, j, item)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)


def load_file(table):
    path= QFileDialog.getOpenFileName(None, "انتخاب فایل", "", "Excel (*.xlsx);;Text (*.txt)")[0]
    if not path: return
    ext = os.path.splitext(path)[1].lower()
    data = []
    if ext == ".xlsx":
        wb = openpyxl.load_workbook(path)
        sh = wb.active
        for row in sh.iter_rows(values_only=True):
            data.append([cell if cell is not None else 0 for cell in row])
    elif ext == ".txt":
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data.append([x for x in line.strip().split(',')])

    available_way = find_way_in_lst(data)
    lst_way = available_way[1] if available_way[0] else None
    display_matrix(table, data, highlight=lst_way)


def create_matrix(table, rows_box, cols_box):
    rows = rows_box.value()
    cols = cols_box.value()
    created_lst = [[randint(0, 1) for _ in range(cols)] for _ in range(rows)]
    available_way = find_way_in_lst(created_lst)
    lst_ways = available_way[1] if available_way[0] else None
    display_matrix(table, created_lst, lst_ways)


def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Finally project")
    win.resize(900, 600)
    win.setStyleSheet("""
        QWidget { background-color: #e8f5e9; font-family: Tahoma; font-size: 14px; }
        QPushButton {
            background-color: #66bb6a; color: white; border-radius: 8px; padding: 10px;
        }
        QPushButton:hover { background-color: #43a047; }
        QSpinBox { background-color: white; padding: 4px; border-radius: 4px; }
    """)

    central = QWidget()
    layout = QVBoxLayout(central)
    control_layout = QHBoxLayout()

    btn_load = QPushButton("📁 Load file")
    rows_box = QSpinBox()
    rows_box.setRange(1, 100)
    rows_box.setValue(5)
    cols_box = QSpinBox()
    cols_box.setRange(1, 100)
    cols_box.setValue(6)
    btn_generate = QPushButton("Create random matrix")

    control_layout.addWidget(btn_load)
    control_layout.addSpacing(30)
    control_layout.addWidget(rows_box)
    control_layout.addWidget(cols_box)
    control_layout.addWidget(btn_generate)

    table = QTableWidget()
    table.setStyleSheet("QTableWidget::item { padding: 10px; }")

    btn_load.clicked.connect(lambda: load_file(table))
    btn_generate.clicked.connect(lambda: create_matrix(table, rows_box, cols_box))

    layout.addLayout(control_layout)
    layout.addWidget(table)
    developer_label = QLabel("Developed by Abolfazl Eskandari")
    developer_label.setAlignment(Qt.AlignCenter)
    developer_label.setStyleSheet("color: #2e7d32; font-size: 12px;")

    github_label = QLabel('<a href="https://github.com/AbalfazlDev">my github</a>')
    github_label.setAlignment(Qt.AlignCenter)
    github_label.setOpenExternalLinks(True)
    github_label.setStyleSheet("color: #2e7d32; font-size: 12px;")

    layout.addWidget(developer_label)
    layout.addWidget(github_label)

    win.setCentralWidget(central)
    win.show()
    sys.exit(app.exec_())


main()
