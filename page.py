# -*- coding: utf-8 -*-

################################################################################
##
## Created by: Yanis
##
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(783, 723)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(430, 340, 171, 181))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.vousLabel = QLabel(self.formLayoutWidget)
        self.vousLabel.setObjectName(u"vousLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.vousLabel)

        self.argentLabel = QLabel(self.formLayoutWidget)
        self.argentLabel.setObjectName(u"argentLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.argentLabel)

        self.miseLabel = QLabel(self.formLayoutWidget)
        self.miseLabel.setObjectName(u"miseLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.miseLabel)

        self.formLayoutWidget_6 = QWidget(self.centralwidget)
        self.formLayoutWidget_6.setObjectName(u"formLayoutWidget_6")
        self.formLayoutWidget_6.setGeometry(QRect(90, 340, 171, 181))
        self.formLayout_6 = QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.vousLabel_5 = QLabel(self.formLayoutWidget_6)
        self.vousLabel_5.setObjectName(u"vousLabel_5")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.vousLabel_5)

        self.argentLabel_2 = QLabel(self.formLayoutWidget_6)
        self.argentLabel_2.setObjectName(u"argentLabel_2")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.argentLabel_2)

        self.miseLabel_2 = QLabel(self.formLayoutWidget_6)
        self.miseLabel_2.setObjectName(u"miseLabel_2")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.miseLabel_2)

        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(550, 90, 171, 181))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.vousLabel_2 = QLabel(self.formLayoutWidget_2)
        self.vousLabel_2.setObjectName(u"vousLabel_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.vousLabel_2)

        self.argentLabel_4 = QLabel(self.formLayoutWidget_2)
        self.argentLabel_4.setObjectName(u"argentLabel_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.argentLabel_4)

        self.miseLabel_4 = QLabel(self.formLayoutWidget_2)
        self.miseLabel_4.setObjectName(u"miseLabel_4")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.miseLabel_4)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 560, 93, 28))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(610, 560, 93, 28))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(390, 560, 93, 28))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(670, 650, 111, 28))
        self.pushButton_3.setCursor(QCursor(Qt.WaitCursor))
        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(701, 449, 31, 171))
        self.verticalSlider.setCursor(QCursor(Qt.ClosedHandCursor))
        self.verticalSlider.setMouseTracking(False)
        self.verticalSlider.setPageStep(5)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setTickPosition(QSlider.TicksBelow)
        self.verticalSlider.setTickInterval(10)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(740, 440, 31, 181))
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(500, 600, 93, 28))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.formLayoutWidget_4 = QWidget(self.centralwidget)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(290, 89, 160, 31))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.potLabel = QLabel(self.formLayoutWidget_4)
        self.potLabel.setObjectName(u"potLabel")

        self.formLayout_4.setWidget(0, QFormLayout.SpanningRole, self.potLabel)

        self.formLayoutWidget_5 = QWidget(self.centralwidget)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(290, 160, 160, 171))
        self.formLayout_5 = QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tableLabel = QLabel(self.formLayoutWidget_5)
        self.tableLabel.setObjectName(u"tableLabel")

        self.formLayout_5.setWidget(0, QFormLayout.SpanningRole, self.tableLabel)

        self.formLayoutWidget_3 = QWidget(self.centralwidget)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(40, 90, 171, 181))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.vousLabel_3 = QLabel(self.formLayoutWidget_3)
        self.vousLabel_3.setObjectName(u"vousLabel_3")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.vousLabel_3)

        self.argentLabel_5 = QLabel(self.formLayoutWidget_3)
        self.argentLabel_5.setObjectName(u"argentLabel_5")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.argentLabel_5)

        self.miseLabel_5 = QLabel(self.formLayoutWidget_3)
        self.miseLabel_5.setObjectName(u"miseLabel_5")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.miseLabel_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 783, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.vousLabel.setText(QCoreApplication.translate("MainWindow", u"Argent :", None))
        self.argentLabel.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.miseLabel.setText(QCoreApplication.translate("MainWindow", u"Mise : ", None))
        self.vousLabel_5.setText(QCoreApplication.translate("MainWindow", u"Argent :", None))
        self.argentLabel_2.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.miseLabel_2.setText(QCoreApplication.translate("MainWindow", u"Mise : ", None))
        self.vousLabel_2.setText(QCoreApplication.translate("MainWindow", u"Argent :", None))
        self.argentLabel_4.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.miseLabel_4.setText(QCoreApplication.translate("MainWindow", u"Mise : ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Parole", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Miser", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Suivre", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Quitter La Table", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10\u20ac</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8\u20ac</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\">6\u20ac</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4\u20ac</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2\u20ac</p></body></html>", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Se Coucher", None))
        self.potLabel.setText(QCoreApplication.translate("MainWindow", u"                Pot", None))
        self.tableLabel.setText(QCoreApplication.translate("MainWindow", u"               Table", None))
        self.vousLabel_3.setText(QCoreApplication.translate("MainWindow", u"Argent :", None))
        self.argentLabel_5.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.miseLabel_5.setText(QCoreApplication.translate("MainWindow", u"Mise : ", None))
    # retranslateUi

