import sys
import datetime  # 需要 pip install datetime
import time
from random import randint
from PySide2.QtWidgets import QApplication, QWidget, QLabel  # pip install PySide2
from PySide2.QtCore import Qt, QObject, Signal
from threading import Thread


class 倒计时信号(QObject):
    信息 = Signal()


class 背诵信号(QObject):
    信息 = Signal()


# 主窗口
class main_win():

    def __init__(self):
        super().__init__()
        self.window = QWidget()
        self.window.resize(456, 412)  # 窗口的大小
        self.window.move(988, 0)  # 窗口的位置
        self.window.setWindowFlag(Qt.FramelessWindowHint)
        self.window.setWindowFlag(Qt.Tool)
        self.window.setWindowFlag(Qt.WindowDoesNotAcceptFocus)
        self.window.setWindowOpacity(0.75)
        self.倒计时 = QLabel(self.window)
        self.倒计时.resize(460, 100)  # 标签的大小
        self.倒计时.move(0, 0)  # 位置
        self.倒计时.setText('''WuW''')
        self.倒计时.setAlignment(Qt.AlignCenter)
        self.倒计时.setStyleSheet('''font-size: 32pt;''')  # 字体大小设置
        self.背诵内容 = QLabel(self.window)
        self.背诵内容.resize(460, 332)  # 标签2的大小
        self.背诵内容.move(0, 100)  # 标签2的位置
        self.背诵内容.setText('''WuW''')
        self.背诵内容.setAlignment(Qt.AlignCenter)
        self.背诵内容.setStyleSheet('''font-size: 32pt;''')  # 字体大小设置
        self.背诵内容.setWordWrap(True)
        self.倒计时信号 = 倒计时信号()
        self.倒计时信号.信息.connect(self.倒计时显示)
        self.倒计时天数 = 0
        self.背诵信号 = 背诵信号()
        self.背诵信号.信息.connect(self.背诵显示)
        self.背诵内容list = []
        with open('./wordsUp.txt', 'r', encoding='utf-8') as f:
            self.data = f.readlines()
        self.data2 = []
        t = Thread(target=self.倒计时函数)
        t1 = Thread(target=self.背诵函数)
        t.start()
        t1.start()

    def 倒计时显示(self):
        self.倒计时.setText(str(self.倒计时天数))

    def 倒计时函数(self):
        while True:
            d = datetime.datetime.now()
            d1 = datetime.datetime(d.year, d.month, d.day, d.hour, d.minute,
                                   d.second)
            d2 = datetime.datetime(2023, 5, 9, 21, 30, 0)  # 结束日期 年 月 日 时 分 秒
            interval = d2 - d1
            h = interval.seconds // (60 * 60)
            m = (interval.seconds - (h * (60 * 60))) // 60
            s = interval.seconds - ((m * 60) + (h * (60 * 60)))
            self.倒计时天数 = f'距离下次考试:\n{interval.days}天{h}时{m}分{s}秒'
            self.倒计时信号.信息.emit()
            time.sleep(1)

    def 背诵显示(self):
        msg = str(self.背诵内容list[2]).replace(r"\n", "\n")
        self.背诵内容.setText(f'{str(self.背诵内容list[0])}:\n{str(self.背诵内容list[1])}\n{msg}')

    def 背诵函数(self):
        while True:
            if len(self.data2) == 0:
                self.data2 = self.data.copy()
            a = self.data2.pop(randint(0, len(self.data2) - 1))
            self.背诵内容list = a.split('|WuW|')
            self.背诵信号.信息.emit()
            time.sleep((len(self.背诵内容list[0])*3))


app = QApplication(sys.argv)
main = main_win()
main.window.show()
sys.exit(app.exec_())