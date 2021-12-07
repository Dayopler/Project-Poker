from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from gui.component.PlayerComponent import PlayerComponent


class Ui_MainWindow(object):

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
        PlayerComponent(name='john', main_window=MainWindow).get()

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

        self.player_2 = QWidget(self.centralwidget)
        self.player_2.setObjectName(u"player_2")
        self.player_2.setGeometry(QRect(290, 0, 181, 181))
        self.horizontalLayoutWidget_6 = QWidget(self.player_2)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(0, 0, 181, 61))
        self.player_infos_2 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.player_infos_2.setObjectName(u"player_infos_2")
        self.player_infos_2.setContentsMargins(0, 0, 0, 0)
        self.player_name_status_2 = QVBoxLayout()
        self.player_name_status_2.setObjectName(u"player_name_status_2")
        self.player_name_2 = QLabel(self.horizontalLayoutWidget_6)
        self.player_name_2.setObjectName(u"player_name_2")

        self.player_name_status_2.addWidget(self.player_name_2)

        self.player_status_2 = QLabel(self.horizontalLayoutWidget_6)
        self.player_status_2.setObjectName(u"player_status_2")

        self.player_name_status_2.addWidget(self.player_status_2)


        self.player_infos_2.addLayout(self.player_name_status_2)

        self.player_money_infos_2 = QHBoxLayout()
        self.player_money_infos_2.setObjectName(u"player_money_infos_2")
        self.player_money_2 = QLabel(self.horizontalLayoutWidget_6)
        self.player_money_2.setObjectName(u"player_money_2")

        self.player_money_infos_2.addWidget(self.player_money_2)


        self.player_infos_2.addLayout(self.player_money_infos_2)

        self.horizontalLayoutWidget_7 = QWidget(self.player_2)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 60, 181, 121))
        self.card_infos_2 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.card_infos_2.setObjectName(u"card_infos_2")
        self.card_infos_2.setContentsMargins(0, 0, 0, 0)
        self.card1_2 = QFrame(self.horizontalLayoutWidget_7)
        self.card1_2.setObjectName(u"card1_2")
        self.card1_2.setFrameShape(QFrame.StyledPanel)
        self.card1_2.setFrameShadow(QFrame.Raised)

        self.card_infos_2.addWidget(self.card1_2)

        self.card2_2 = QFrame(self.horizontalLayoutWidget_7)
        self.card2_2.setObjectName(u"card2_2")
        self.card2_2.setFrameShape(QFrame.StyledPanel)
        self.card2_2.setFrameShadow(QFrame.Raised)

        self.card_infos_2.addWidget(self.card2_2)

        self.player_3 = QWidget(self.centralwidget)
        self.player_3.setObjectName(u"player_3")
        self.player_3.setGeometry(QRect(590, 0, 181, 181))
        self.horizontalLayoutWidget_10 = QWidget(self.player_3)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(0, 0, 181, 61))
        self.player_infos_4 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.player_infos_4.setObjectName(u"player_infos_4")
        self.player_infos_4.setContentsMargins(0, 0, 0, 0)
        self.player_name_status_4 = QVBoxLayout()
        self.player_name_status_4.setObjectName(u"player_name_status_4")
        self.player_name_4 = QLabel(self.horizontalLayoutWidget_10)
        self.player_name_4.setObjectName(u"player_name_4")

        self.player_name_status_4.addWidget(self.player_name_4)

        self.player_status_4 = QLabel(self.horizontalLayoutWidget_10)
        self.player_status_4.setObjectName(u"player_status_4")

        self.player_name_status_4.addWidget(self.player_status_4)


        self.player_infos_4.addLayout(self.player_name_status_4)

        self.player_money_infos_4 = QHBoxLayout()
        self.player_money_infos_4.setObjectName(u"player_money_infos_4")
        self.player_money_4 = QLabel(self.horizontalLayoutWidget_10)
        self.player_money_4.setObjectName(u"player_money_4")

        self.player_money_infos_4.addWidget(self.player_money_4)


        self.player_infos_4.addLayout(self.player_money_infos_4)

        self.horizontalLayoutWidget_11 = QWidget(self.player_3)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(0, 60, 181, 121))
        self.card_infos_4 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.card_infos_4.setObjectName(u"card_infos_4")
        self.card_infos_4.setContentsMargins(0, 0, 0, 0)
        self.card1_4 = QFrame(self.horizontalLayoutWidget_11)
        self.card1_4.setObjectName(u"card1_4")
        self.card1_4.setFrameShape(QFrame.StyledPanel)
        self.card1_4.setFrameShadow(QFrame.Raised)

        self.card_infos_4.addWidget(self.card1_4)

        self.card2_4 = QFrame(self.horizontalLayoutWidget_11)
        self.card2_4.setObjectName(u"card2_4")
        self.card2_4.setFrameShape(QFrame.StyledPanel)
        self.card2_4.setFrameShadow(QFrame.Raised)

        self.card_infos_4.addWidget(self.card2_4)

        self.player_4 = QWidget(self.centralwidget)
        self.player_4.setObjectName(u"player_4")
        self.player_4.setGeometry(QRect(800, 190, 181, 181))
        self.horizontalLayoutWidget_12 = QWidget(self.player_4)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(0, 0, 181, 61))
        self.player_infos_5 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.player_infos_5.setObjectName(u"player_infos_5")
        self.player_infos_5.setContentsMargins(0, 0, 0, 0)
        self.player_name_status_5 = QVBoxLayout()
        self.player_name_status_5.setObjectName(u"player_name_status_5")
        self.player_name_5 = QLabel(self.horizontalLayoutWidget_12)
        self.player_name_5.setObjectName(u"player_name_5")

        self.player_name_status_5.addWidget(self.player_name_5)

        self.player_status_5 = QLabel(self.horizontalLayoutWidget_12)
        self.player_status_5.setObjectName(u"player_status_5")

        self.player_name_status_5.addWidget(self.player_status_5)


        self.player_infos_5.addLayout(self.player_name_status_5)

        self.player_money_infos_5 = QHBoxLayout()
        self.player_money_infos_5.setObjectName(u"player_money_infos_5")
        self.player_money_5 = QLabel(self.horizontalLayoutWidget_12)
        self.player_money_5.setObjectName(u"player_money_5")

        self.player_money_infos_5.addWidget(self.player_money_5)


        self.player_infos_5.addLayout(self.player_money_infos_5)

        self.horizontalLayoutWidget_13 = QWidget(self.player_4)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(0, 60, 181, 121))
        self.card_infos_5 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.card_infos_5.setObjectName(u"card_infos_5")
        self.card_infos_5.setContentsMargins(0, 0, 0, 0)
        self.card1_5 = QFrame(self.horizontalLayoutWidget_13)
        self.card1_5.setObjectName(u"card1_5")
        self.card1_5.setFrameShape(QFrame.StyledPanel)
        self.card1_5.setFrameShadow(QFrame.Raised)

        self.card_infos_5.addWidget(self.card1_5)

        self.card2_5 = QFrame(self.horizontalLayoutWidget_13)
        self.card2_5.setObjectName(u"card2_5")
        self.card2_5.setFrameShape(QFrame.StyledPanel)
        self.card2_5.setFrameShadow(QFrame.Raised)

        self.card_infos_5.addWidget(self.card2_5)

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
        self.player_name_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_status_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_money_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_name_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_status_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_money_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_name_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_status_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_money_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Seed", None))
    # retranslateUi

