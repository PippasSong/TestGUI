# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')  # 타이틀바에 나타나는 창의 제목

        self.setWindowIcon(QIcon('icon.jpg'))  # 아이콘 파일

        btn_quit = QPushButton('Quit', self)  # 푸시버튼을 하나 만든다. 첫번째 파라미터: 버튼에 표시될 텍스트 두번째 파라미터: 버튼이 위치할 부모 위젯
        btn_quit.move(50, 50)
        btn_quit.resize(btn_quit.sizeHint())
        # btn을 클릭하면 clicked 시그널이 만들어진다.
        # instance() 메서드는 현재 인스턴스(btn?)를 반환
        # clicked 시그널은 어플리케이션을 종료하는 quit메서드에 연결
        btn_quit.clicked.connect(QCoreApplication.instance().quit)

        QToolTip.setFont(QFont('SansSerif', 10))  # 툴팁에 사용될 폰트
        self.setToolTip('This is a <b>QWidget</b> widget')  # 툴팁을 만들기 위해 settooltip 메소드 사용해 표시될 텍스트 입력
        btn_tooltip = QPushButton('Button', self)
        btn_tooltip.setToolTip('This is a <b>QPushButton</b> widget')  # 버튼에 툴팁 달기
        btn_tooltip.move(200, 50)
        btn_tooltip.resize(btn_tooltip.sizeHint())  # sizehint 메소드는 버튼을 적절한 크기로 설정하도록 도와준다

        # self.move(300, 300) # 위젯을 스크린의 x=300px, y=300px의 위치로 이동시킴
        # self.resize(400, 200) # 위젯의 크기를 너비 400px 높이 200px로 조정
        self.setGeometry(300, 300, 600, 400)  # 창의 x, y 위치, 창의 너비, 높이
        self.show()  # 위젯을 스크린에 보여줌


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야함
    ex = MyApp()
    sys.exit(app.exec_())


