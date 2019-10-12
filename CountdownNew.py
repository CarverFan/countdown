from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import datetime


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Countdown")

        layout = QVBoxLayout()

        label = QLabel("Select Date")
        label.setAlignment(Qt.AlignCenter)

        dtEdit = QDateTimeEdit()
        dtEdit.setDateTime(QDateTime.currentDateTime())

        dtEdit.setCalendarPopup(True)
        dtEdit.dateTimeChanged.connect(self.dt_changed)

        label1 = QLabel("Days Remaining")
        label1.setAlignment(Qt.AlignCenter)

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(3)
        self.lcd.display(0)

        layout.addWidget(label)
        layout.addWidget(dtEdit)
        layout.addWidget(label1)
        layout.addWidget(self.lcd)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def dt_changed(self, dt):
        print("DT Changed")
        today = datetime.datetime.now()
        print("Python DT: ", today)
        print("PyQt DT: ", dt)

        print("DT Converted")
        pydt = dt.toPyDateTime()
        print(pydt)

        dtdelta = pydt - today
        print("delta: ", dtdelta)
        dtdelta_str = str(dtdelta)
        print(dtdelta_str)
        self.lcd.display(dtdelta_str[0:3])
        self.lcd.repaint()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
