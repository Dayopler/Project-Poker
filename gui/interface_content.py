from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from gui.component.PlayerComponent import PlayerComponent
from random import randint


class Ui_MainWindow(object):

    def __init__(self):
        self.players: list[PlayerComponent] = []
        player_place: int = randint(0, 3)

        for i in range(0, 4):
            if player_place == i:
                self.players.append(PlayerComponent(name=f'PlayerName', is_ia=False, position_index=i))
            else:
                self.players.append(PlayerComponent(name=f'IA-{i}', position_index=i))

    def setupUi(self, MainWindow):
        MainWindow.resize(1011, 581)
        MainWindow.setStyleSheet(u"")

        """
        =============================
        toolbar action
        =============================
        """
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")

        """
        =============================
        player component
        =============================
        """
        for player in self.players:
            player.get(MainWindow)

        """
        =============================
        card revealed
        =============================
        """
        self.card_revealed_infos = QWidget(self.centralwidget)
        self.card_revealed_infos.setObjectName(u"card_revealed_infos")
        self.card_revealed_infos.setGeometry(QRect(270, 200, 481, 171))
        self.horizontalLayoutWidget_4 = QWidget(self.card_revealed_infos)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 0, 481, 171))
        self.card_revealed_container = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.card_revealed_container.setObjectName(u"card_revealed_container")
        self.card_revealed_container.setContentsMargins(0, 0, 0, 0)
        self.card_revealed_1 = QFrame(self.horizontalLayoutWidget_4)
        self.card_revealed_1.setObjectName(u"card_revealed_1")
        self.card_revealed_1.setFrameShape(QFrame.StyledPanel)
        self.card_revealed_1.setFrameShadow(QFrame.Raised)

        self.card_revealed_container.addWidget(self.card_revealed_1)

        self.card_revealed_2 = QFrame(self.horizontalLayoutWidget_4)
        self.card_revealed_2.setObjectName(u"card_revealed_2")
        self.card_revealed_2.setFrameShape(QFrame.StyledPanel)
        self.card_revealed_2.setFrameShadow(QFrame.Raised)

        self.card_revealed_container.addWidget(self.card_revealed_2)

        self.card_revealed_3 = QFrame(self.horizontalLayoutWidget_4)
        self.card_revealed_3.setObjectName(u"card_revealed_3")
        self.card_revealed_3.setFrameShape(QFrame.StyledPanel)
        self.card_revealed_3.setFrameShadow(QFrame.Raised)

        self.card_revealed_container.addWidget(self.card_revealed_3)

        self.card_revealed_4 = QFrame(self.horizontalLayoutWidget_4)
        self.card_revealed_4.setObjectName(u"card_revealed_4")
        self.card_revealed_4.setFrameShape(QFrame.StyledPanel)
        self.card_revealed_4.setFrameShadow(QFrame.Raised)

        self.card_revealed_container.addWidget(self.card_revealed_4)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 429, 991, 91))
        self.button_group = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.button_group.setObjectName(u"button_group")
        self.button_group.setContentsMargins(0, 0, 0, 0)
        self.button_follow = QPushButton(self.horizontalLayoutWidget_5)
        self.button_follow.setObjectName(u"button_follow")

        self.button_group.addWidget(self.button_follow)

        self.button_bet = QPushButton(self.horizontalLayoutWidget_5)
        self.button_bet.setObjectName(u"button_bet")

        self.button_group.addWidget(self.button_bet)

        self.button_fold = QPushButton(self.horizontalLayoutWidget_5)
        self.button_fold.setObjectName(u"button_fold")

        self.button_group.addWidget(self.button_fold)

        self.button_parole = QPushButton(self.horizontalLayoutWidget_5)
        self.button_parole.setObjectName(u"button_parole")

        self.button_group.addWidget(self.button_parole)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1011, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load seed", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save seed", None))
        self.button_follow.setText(QCoreApplication.translate("MainWindow", u"Follow", None))
        self.button_bet.setText(QCoreApplication.translate("MainWindow", u"Bet", None))
        self.button_fold.setText(QCoreApplication.translate("MainWindow", u"Fold", None))
        self.button_parole.setText(QCoreApplication.translate("MainWindow", u"Faire Parole", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Seed", None))
    # retranslateUi

