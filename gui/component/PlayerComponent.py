from gui.component.CardComponent import CardComponent
from PokerGame import Player
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class PlayerComponent(Player):
    def __init__(self, name: str, main_window):
        super().__init__(name)
        self.__cards_component = [CardComponent(), CardComponent()]
        self.__main_window = main_window

    def __repr__(self):
        return 'player component'

    def get(self):
        """
        return the component build
        :return:
        """
        # set up the widget
        self.player = QWidget(self.__main_window)
        self.player.setObjectName(u"player")
        self.player.setGeometry(QRect(20, 180, 181, 181))

        # horizontal container
        self.horizontalLayoutWidget = QWidget(self.player)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 181, 61))

        # player infos for player name and status (is ia or not)
        self.player_infos = QHBoxLayout(self.horizontalLayoutWidget)
        self.player_infos.setObjectName(u"player_infos")
        self.player_infos.setContentsMargins(0, 0, 0, 0)

        self.player_name_status = QVBoxLayout()
        self.player_name_status.setObjectName(u"player_name_status")

        # set player name
        self.player_name = QLabel(self.horizontalLayoutWidget)
        self.player_name.setObjectName(u"player_name")
        self.player_name_status.addWidget(self.player_name)
        self.player_name.setText(QCoreApplication.translate("MainWindow", self.name, None))

        # set player status
        self.player_status = QLabel(self.horizontalLayoutWidget)
        self.player_status.setObjectName(u"player_status")
        self.player_status.setText(QCoreApplication.translate("MainWindow", u"IA" if self.is_ia else u"You", None))
        self.player_name_status.addWidget(self.player_status)


        self.player_infos.addLayout(self.player_name_status)

        # money player have
        self.player_money_infos = QHBoxLayout()
        self.player_money_infos.setObjectName(u"player_money_infos")
        self.player_money = QLabel(self.horizontalLayoutWidget)
        self.player_money.setObjectName(u"player_money")

        self.player_money_infos.addWidget(self.player_money)
        self.player_money.setText(QCoreApplication.translate("MainWindow", str(self.money), None))
        self.player_infos.addLayout(self.player_money_infos)

        self.horizontalLayoutWidget_3 = QWidget(self.player)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 60, 181, 121))

        # first card graphic representation
        self.card_infos = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.card_infos.setObjectName(u"card_infos")
        self.card_infos.setContentsMargins(0, 0, 0, 0)
        self.card1 = QFrame(self.horizontalLayoutWidget_3)
        self.card1.setObjectName(u"card1")
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)

        self.card_infos.addWidget(self.card1)

        # second card graphic representation
        self.card2 = QFrame(self.horizontalLayoutWidget_3)
        self.card2.setObjectName(u"card2")
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)

        self.card_infos.addWidget(self.card2)