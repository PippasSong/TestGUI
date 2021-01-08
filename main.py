# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDate, Qt, QTime, QDateTime


class MyApp(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
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
        # self.setToolTip('This is a <b>QWidget</b> widget')  # 툴팁을 만들기 위해 settooltip 메소드 사용해 표시될 텍스트 입력
        btn_tooltip = QPushButton('Button', self)
        btn_tooltip.setToolTip('This is a <b>QPushButton</b> widget')  # 버튼에 툴팁 달기
        btn_tooltip.move(200, 50)
        btn_tooltip.resize(btn_tooltip.sizeHint())  # sizehint 메소드는 버튼을 적절한 크기로 설정하도록 도와준다

        # 상태바 만들기
        # qmainwindow클래스의 statusbar 메소드 사용
        # 메세지 텍스트 가지고 오기: currentMessage()
        # self.statusBar().showMessage('Ready')

        # 메뉴바 만들기
        # exit라벨을 갖는 하나의 동작을 만들고 단축키, 상태바 상태팁 를 정의
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)  # 위젯의 quit 메서드에 연결

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')  # 'File'메뉴 생성 '&'는 간편하게 단축키를 설정하게 해줌(F앞에 앰퍼샌드가 있으므로 'Alt+F'가 File메뉴의 단축키)
        filemenu.addAction(exitAction)  # exitAction 동작 추가

        # 툴바 만들기
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # self.move(300, 300) # 위젯을 스크린의 x=300px, y=300px의 위치로 이동시킴
        # self.resize(400, 200) # 위젯의 크기를 너비 400px 높이 200px로 조정
        self.setGeometry(300, 300, 600, 400)  # 창의 x, y 위치, 창의 너비, 높이

        # 창을 화면의 가운데로
        self.center()

        # 현재 날짜 형식 설정
        now = QDate.currentDate()
        print(now.toString('d.M.yy'))
        print(now.toString('dd.MM.yyyy'))
        print(now.toString('ddd.MMMM.yyyy'))
        print(now.toString(Qt.ISODate)) # ISO 표준 형식
        print(now.toString(Qt.DefaultLocaleLongDate)) # 어플리케이션의 기본 설정

        # 시간 형식 설정
        time = QTime.currentTime()
        print(time.toString())
        print(time.toString('h.m.s'))
        print(time.toString('hh.mm.ss'))
        print(time.toString('hh.mm.ss.zzz')) #z는 1000분의 1초
        print(time.toString(Qt.DefaultLocaleLongDate))
        print(time.toString(Qt.DefaultLocaleShortDate))

        # 날짜와 시간 표시
        datetime = QDateTime.currentDateTime()
        print(datetime.toString())
        print(datetime.toString('d.M.yy hh:mm:ss'))
        print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
        print(datetime.toString(Qt.DefaultLocaleLongDate))
        print(datetime.toString(Qt.DefaultLocaleShortDate))

        # 상태표시줄에 날짜 표시
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))



        self.show()  # 위젯을 스크린에 보여줌

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center() # 사용하는 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp) # 창의 직사각형 위치를 화면의 중심 위치로 이동
        self.move(qr.topLeft()) # 현재 창을 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동



if __name__ == '__main__':
    app = QApplication(sys.argv)  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야함
    ex = MyApp()
    sys.exit(app.exec_())
