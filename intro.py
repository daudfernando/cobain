# sambungin modul
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout

# bikin objek kelasnya
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('My first app')
my_win.move(900, 70)
my_win.resize(400, 200)
my_win.show()

# posisi widgetnya
line = QHBoxLayout()
title = QLabel('Hello, world!')

# tampilan aplikasinya
line.addWidget(title, alignment=Qt.AlignCenter)
my_win.setLayout(line)
app.exec_()