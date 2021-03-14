import sys
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QLineEdit, QDialog
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtGui import *
import random

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("차오차오")
        self.resize(1600, 900)

        self.lbl = QLabel(self)
        self.lbl.resize(1700, 500)
        pixmap = QPixmap("background.png")
        self.lbl.setPixmap(QPixmap(pixmap))
        self.lbl.move(0, 200)

        #label
        self.title = QLabel(self)
        self.title.setAlignment(Qt.AlignCenter) #수평수직으로 맞춰줌
        self.title.move(650, 100)
        self.title.resize(300, 100)
        self.title.setText("차오차오")
        self.title.setFont(QtGui.QFont("맑은 고딕", 35))

        #시작화면 버튼
        self.rulebtn = QPushButton("GameRule", self)
        self.rulebtn.move(300, 600)
        self.rulebtn.resize(300, 150)
        self.rulebtn.clicked.connect(self.GameRule)
        self.startbtn = QPushButton('GameStart', self)
        self.startbtn.move(1000, 600)
        self.startbtn.resize(300, 150)
        self.startbtn.clicked.connect(self.game_start)

        #다이얼로그
        self.dialog = QDialog()

    def game_start(self):
        self.start = MainGame()
        self.start.show()

    def ButtonUI(self):
        self.label.setText("GameRule")

    def GameRule(self):


        titlelbl = QLabel(self.dialog)
        titlelbl.setText("차오차오 GameRule 설명")
        titlelbl.move(600, 0)
        titlelbl.setFont(QtGui.QFont("맑은 고딕", 20))

        label = QLabel(self.dialog)
        label.setText("게임 인원>> 2명\n\n준비물>> 컴퓨터 1대"+
        "\n\n게임 배경>> 여러분에게는 5명의 모험가가 주어집니다. \n여러분 앞에는 식충식물이 우글거리는 늪지대가 기다리고 있습니다."
        "\n 과연 여러분은 이곳에서 살아남을 수 있을까요?\n\n"
        "게임목표>>한 명당 5명의 모험가가 주어집니다. 자신의 모험가들 3명이 먼저 다리를 건너면 승리합니다.또는 점수를 많이 얻는 사람이 승리하게 됩니다.\n\n"
        "게임방법>>1. 먼저 게임참여자 2명은 각각 누가 Player1을 할지, Player2를 할지 결정해주세요.\n"
        "Player를 정했다면 자신의 차례에 '주사위 던지기'버튼을 이용하여 주사위를 굴립니다. 그 후 자신만 주사위를 확인합니다.\n"
        "2. 숫자를 확인한 플레이어는 숫자를 말해야하는데 1~4까지만 말할 수 있습니다. 중요한 것은 내가 말한 숫자만큼 움직일 수 있다는 것입니다.\n"
        "3. 주사위 숫자를 확인하지 않은 플레이어는 그 사람이 말한 숫자를 믿을 것인지,믿지 않을 것인지 결정해야합니다.\n"
        "4. 믿는다면? 주사위의 숫자를 확인하지 않은 채로 다음 플레이어가 주사위를 돌리면 됩니다.\n 믿지 않는다면? '챠오챠오'버튼을 클릭해서 주사위에 나온 값을 확인해주세요.\n"
        "*숫자를 선언한 사람이 정직했다면 의심한 플레이어의 말이 다리 아래 늪지대로 떨어뜨립니다. 이때, 말로 '챠오챠오'라고 인사해주세요 \n"
        "그리고 선언한 사람은 말한 숫자만큼 자신의 말을 전진시킵니다. *숫자를 선언한 사람이 정직하지 못했다면 숫자를 선언한 사람의 게임 말을 다리 밑으로 떨어뜨립니다.\n\n"
        "if 주사위에서 X표시가 나왔다면? X표시가 나온다면 무조건 거짓말을 해야합니다."
        "\n숫자는 1~4까지로 적을 수 있으며, 어떤 말을 해야 상대방이 믿을지 신중히 생각하고 적어야합니다.\n\n"
        "게임 종료>>누군가 한사람의 말 3개가 다리를 건너면 게임이 끝나고 그 플레이어가 승리하게 됩니다.\n"
        "이때, 누구도 3개를 건널 수 없는 상황이라면 끝까지 플레이하여 점수가 가장 높은 사람이 승리합니다")
        label.move(50, 70)
        label.resize(1550, 800)
        label.setFont(QtGui.QFont("맑은 고딕", 12))

        # QDialog 세팅
        self.dialog.setWindowTitle('게임룰 설명')
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(1600, 900)
        self.dialog.show()

    # Dialog 닫기 이벤트
    def dialog_close(self):
        self.dialog.close()

class MainGame(QMainWindow): #QMainWindow를 상속받음

    def __init__(self):
        super().__init__()
        self.resize(1600, 900) #사이즈설정

        MainGame.p1x = 0
        MainGame.p2x = 0

        MainGame.dicScore = {}
        MainGame.dicScoreNum = 0

        self.demoWidget()
        self.player()

        Player.orderWho = 'p2'

    def demoWidget(self):
        self.label = QLabel("플레이어",self)
        self.label.setFont(QtGui.QFont('Agency FB',10))
        self.label.move(800,20)
        self.btn1 = QPushButton("주사위",self)
        self.btn1.setFont(QtGui.QFont('SanSerif',14))
        self.btn1.resize(136,30)
        self.btn1.move(600,20)
        self.btn1.clicked.connect(self.button_clicked)
        self.btn2 = QPushButton("차오차오", self)
        self.btn2.setFont(QtGui.QFont('SanSerif', 13))
        self.btn2.resize(136, 30)
        self.btn2.move(930, 20)
        self.btn2.clicked.connect(self.button_clicked2)

        self.lbl = QLabel(self)
        self.lbl.resize(1700,500)
        pixmap = QPixmap("background.png")
        self.lbl.setPixmap(QPixmap(pixmap))
        self.lbl.move(0, 200)

        # 승패출력 칸
        MainGame.lbScore = QLabel("", self)
        MainGame.lbScore.setAlignment(Qt.AlignTop)
        MainGame.lbScore.resize(110, 190)
        MainGame.lbScore.move(1460, 5)

    def player(self):
        MainGame.p1 = QLabel(self)
        MainGame.p1.resize(90,150)
        pixmap = QPixmap("player1.png")
        MainGame.p1.setPixmap(QPixmap(pixmap))
        MainGame.p1.move(30, 280)

        MainGame.p2 = QLabel(self)
        MainGame.p2.resize(90, 150)
        pixmap = QPixmap("player2.png")
        MainGame.p2.setPixmap(QPixmap(pixmap))
        MainGame.p2.move(30, 430)

        self.lb1 = QLabel("플레이어1", self)
        self.lb1.move(10, 10)
        self.lb2 = QLabel("플레이어2", self)
        self.lb2.move(10, 30)

        MainGame.p1Piece = 5
        MainGame.p2Piece = 5
        MainGame.lb1N = QLabel(str(MainGame.p1Piece), self)
        MainGame.lb1N.move(100, 10)
        MainGame.lb2N = QLabel(str(MainGame.p2Piece), self)
        MainGame.lb2N.move(100, 30)

    def button_clicked(self):
        self.dice = Dice()
        self.dice.show()

        if(Player.orderWho == 'p2'):
            Player.orderWho = 'p1'
            self.label.setText("플레이어1")
        elif(Player.orderWho == 'p1'):
            Player.orderWho = 'p2'
            self.label.setText("플레이어2")

    def button_clicked2(self):
        self.chao = Chaobtn()
        self.chao.show()

#주사위 클래스
class Dice(QtWidgets.QWidget):  # QWidget 상속

    def __init__(self):
        super().__init__()

        self.s = 0
        Dice.diceNum = 0

        #주사위 값 배열
        self.dice = ["X", "1", "2", "3", "4", "X"]

        self.diceUI()

    def diceUI(self):
        # 주사위돌리기
        self.button = QtWidgets.QPushButton("주사위 돌리기")  # 버튼 객체 생성
        self.text = QtWidgets.QLabel("당신의 주사위 값은??")  # 라벨 객체 생성
        self.text.setAlignment(QtCore.Qt.AlignCenter)  # 정렬

        # X일때 숫자 입력
        self.Xlabel = QLabel("자신이 돌린 주사위의 값을 입력해주세요: \n (이때,X값이 나오면 1~4까지의 숫자를 입력해주세요)", self)
        self.Xlabel.move(20, 20)
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 20)
        self.lineEdit.textChanged.connect(self.lineEditChanged)
        self.text2 = QtWidgets.QLabel("X의 주사위값: ")
        self.statusBar = QtWidgets.QStatusBar(self)

        # 각 레이아웃 적용
        self.layout = QtWidgets.QVBoxLayout()  # 레이아웃 객체 생성
        self.layout.addWidget(self.text)  # 레이아웃에 라벨 설정
        self.layout.addWidget(self.button)  # 레이아웃에 버튼 설정
        self.layout.addWidget(self.Xlabel)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.text2)
        self.layout.addWidget(self.statusBar)
        self.setLayout(self.layout)  # 위젯에 레이아웃 설정

        self.button.clicked.connect(self.changedice)  # 버튼 이벤트

    def changedice(self):
        self.s = random.choice(self.dice) #랜덤 choice -> 랜덤 값 하나 가져오기
        self.text.setText(self.s) #주사위 값
        self.button.setDisabled(True) #버튼 비활성화

    def lineEditChanged(self):
        if(self.lineEdit.text() != ''):
            if(self.s == 'X'):
                if(1<=int(self.lineEdit.text())<=4):
                    Dice.diceNum = int(self.lineEdit.text()) #X값일 때의 주사위값
                    self.statusBar.showMessage(str(Dice.diceNum))
                else:
                    self.statusBar.showMessage("1~4까지의 숫자를 입력해주세요")
            else:
                Dice.diceNum = self.s
                self.statusBar.showMessage(str(Dice.diceNum))

    def closeEvent(self, event):
        self.deleteLater()
        event.accept()
        Player().playerMove(Player.orderWho)

class Chaobtn(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.chaoUI()

        # self.s = Dice.diceNum

    def chaoUI(self):
        self.text = QtWidgets.QLabel("플레이어끼리 주사위 수를 확인해주세요")  # 라벨 객체 생성
        self.text.setAlignment(QtCore.Qt.AlignCenter)  # 정렬
        self.diebtn = QtWidgets.QPushButton("거짓말이었다면 버튼 클릭")
        self.diebtn.clicked.connect(self.deadbtn)

        # 각 레이아웃 적용
        self.layout = QtWidgets.QVBoxLayout()  # 레이아웃 객체 생성
        self.layout.addWidget(self.text)  # 레이아웃에 라벨 설정
        self.layout.addWidget(self.diebtn)  # 레이아웃에 버튼 설정
        self.setLayout(self.layout)  # 위젯에 레이아웃 설정

    def deadbtn(self):
        self.movex = [30, 190, 330, 470, 610, 750, 900, 1040, 1190, 1330, 1490]  # array 생성 x좌표

        if (Player.orderWho == 'p1'):
            MainGame.p1.move(self.movex[0], 280)
            MainGame.p1Piece -= 1
            MainGame.p1x = 0
            MainGame.lb1N.setText(str(MainGame.p1Piece))
        elif (Player.orderWho == 'p2'):
            MainGame.p2.move(self.movex[0], 430)
            MainGame.p2Piece -= 1
            MainGame.p2x = 0
            MainGame.lb2N.setText(str(MainGame.p2Piece))

#플레이어 기능
class Player:
    def __init__(self):
        self.xnum = Dice.diceNum #사용자 입력 값

    def playerMove(self, who):
        self.movex = [30, 190, 330, 470, 610, 750, 900, 1040, 1190, 1330, 1490]  # array 생성 x좌표

        if (who == 'p1'):
            MainGame.p1x += int(self.xnum)  # num 자리에 주사위값을 넣으면 돼
            if(MainGame.p1x > 10) : MainGame.p1x = 10
            MainGame.p1.move(self.movex[MainGame.p1x], 280)
            self.dead(who)
        elif (who == 'p2'):
            MainGame.p2x += int(self.xnum)
            if (MainGame.p2x > 10): MainGame.p2x = 10
            MainGame.p2.move(self.movex[MainGame.p2x], 430)
            self.dead(who)

    def dead(self, who):
        if (MainGame.p1x == MainGame.p2x and MainGame.p1x != 0 and MainGame.p2x != 0
                and MainGame.p1x != 10 and MainGame.p2x != 10):
            if (who == 'p1'):
                MainGame.p2.move(self.movex[0], 430)
                MainGame.p2Piece -= 1
                MainGame.p2x = 0
                MainGame.lb2N.setText(str(MainGame.p2Piece))
            elif (who == 'p2'):
                MainGame.p1.move(self.movex[0], 280)
                MainGame.p1Piece -= 1
                MainGame.p1x = 0
                MainGame.lb1N.setText(str(MainGame.p1Piece))

        if (MainGame.p1x == 10):
            MainGame.p1.move(self.movex[0], 280)
            MainGame.p1Piece -= 1
            MainGame.p1x = 0
            MainGame.lb1N.setText(str(MainGame.p1Piece))
            Result.score(Result(), who)
        elif (MainGame.p2x == 10):
            MainGame.p2.move(self.movex[0], 430)
            MainGame.p2Piece -= 1
            MainGame.p2x = 0
            MainGame.lb2N.setText(str(MainGame.p2Piece))
            Result.score(Result(), who)

    def order(self): #순서처리
        Player.orderWho = ''

class Result:
    def __init__(self):
        self.scoreStr = ""

    # 화면에 출력하는 도착순서
    def score(self, who):
        MainGame.dicScoreNum += 1

        if(who == 'p1'):
            MainGame.dicScore[MainGame.dicScoreNum] = '플레이어1'
        elif(who == 'p2'):
            MainGame.dicScore[MainGame.dicScoreNum] = '플레이어2'

        # 딕셔너리의 key와 value값 가져오기
        for key, value in MainGame.dicScore.items():
            self.scoreStr += (str(key) + "등 : " + value + "\n")
        MainGame.lbScore.setText(self.scoreStr)

        self.File()

    def File(self):
        f = open("WinLose.txt", 'a')

        count1 = 0; count2 = 0
        score1 = 0; score2 = 0
        fileStr = ""

        for value in MainGame.dicScore.values():
            if (value == '플레이어1'):
                count1 += 1
            elif (value == '플레이어2'):
                count2 += 1

            if (count1 >= 3 or count2 >= 3):
                if (count1 >= 3):
                    fileStr = "승\t패\n"
                elif (count2 >= 3):
                    fileStr = "패\t승\n"
            else:
                if(MainGame.p2Piece == 0 or MainGame.p1Piece == 0):
                    num = 11
                    for key, value in MainGame.dicScore.items():
                        if (value == '플레이어1'):
                            score1 += (num-key)
                        elif (value == '플레이어2'):
                            score2 += (num-key)
                    if(score1 > score2) : fileStr = "승\t패\n"
                    else: fileStr = "패\t승\n"
        f.write(fileStr)
        f.close()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w1 = MyWindow()
    w1.show()

    sys.exit(app.exec_())