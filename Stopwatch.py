import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout 
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("START", self)
        self.stop_button = QPushButton("STOP", self)
        self.reset_button = QPushButton("RESET", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.start_button.setObjectName("startb")
        self.stop_button.setObjectName("stopb")
        self.reset_button.setObjectName("resetb")

        self.setStyleSheet("""
                QPushButton, QLabel{
                    padding: 20px;
                    font-weight: bold;
                    font-famil: calibri;
                           }
                QPushButton{
                    font-size: 50px;
                    border: 3px solid;
                    border-radius: 15px;
                           }
                QPushButton#startb{
                    background: hsl(120, 100%, 54%)
                           }
                QPushButton#stopb{
                    background: hsl(6, 100%, 54%)
                           }
                QPushButton#resetb{
                    background: hsl(302, 2%, 43%)
                           }
                QPushButton#startb:hover{
                    background: hsl(120, 100%, 74%)
                           }
                QPushButton#stopb:hover{
                    background: hsl(6, 100%, 74%)
                           }
                QPushButton#resetb:hover{
                    background: hsl(302, 2%, 63%)
                           }
                QLabel{
                    font-size: 120px;
                    background-color: hsl(200, 100%, 85%);
                    border-radius: 20px;
                           }
                
            """)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        millisec = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{millisec:02}"

    def update(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())