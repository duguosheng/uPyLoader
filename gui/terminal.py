# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'terminal.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLayout,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTextEdit, QVBoxLayout, QWidget)

class Ui_TerminalDialog(object):
    def setupUi(self, TerminalDialog):
        if not TerminalDialog.objectName():
            TerminalDialog.setObjectName(u"TerminalDialog")
        TerminalDialog.resize(1196, 394)
        TerminalDialog.setModal(False)
        self.horizontalLayout_3 = QHBoxLayout(TerminalDialog)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.splitter = QSplitter(TerminalDialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setLineWidth(0)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(6)
        self.verticalLayoutWidget_3 = QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.outputTextEdit = QTextEdit(self.verticalLayoutWidget_3)
        self.outputTextEdit.setObjectName(u"outputTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputTextEdit.sizePolicy().hasHeightForWidth())
        self.outputTextEdit.setSizePolicy(sizePolicy)
        self.outputTextEdit.setFocusPolicy(Qt.ClickFocus)
        self.outputTextEdit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.outputTextEdit.setCursorWidth(0)
        self.outputTextEdit.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.outputTextEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.autoscrollCheckBox = QCheckBox(self.verticalLayoutWidget_3)
        self.autoscrollCheckBox.setObjectName(u"autoscrollCheckBox")

        self.horizontalLayout_2.addWidget(self.autoscrollCheckBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.clearButton = QPushButton(self.verticalLayoutWidget_3)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout_2.addWidget(self.clearButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.verticalLayoutWidget_3)
        self.horizontalLayoutWidget = QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalLayoutWidget.sizePolicy().hasHeightForWidth())
        self.horizontalLayoutWidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.inputTextBox = QPlainTextEdit(self.horizontalLayoutWidget)
        self.inputTextBox.setObjectName(u"inputTextBox")
        sizePolicy.setHeightForWidth(self.inputTextBox.sizePolicy().hasHeightForWidth())
        self.inputTextBox.setSizePolicy(sizePolicy)
        self.inputTextBox.setMinimumSize(QSize(0, 10))
        self.inputTextBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.inputTextBox.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.horizontalLayout.addWidget(self.inputTextBox)

        self.sendButton = QPushButton(self.horizontalLayoutWidget)
        self.sendButton.setObjectName(u"sendButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy2)
        self.sendButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.sendButton)

        self.splitter.addWidget(self.horizontalLayoutWidget)

        self.verticalLayout.addWidget(self.splitter)

        self.horizontalSpacer_2 = QSpacerItem(40, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.line = QFrame(TerminalDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.groupBox = QGroupBox(TerminalDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setMinimumSize(QSize(100, 0))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ctrlaButton = QPushButton(self.groupBox)
        self.ctrlaButton.setObjectName(u"ctrlaButton")
        sizePolicy2.setHeightForWidth(self.ctrlaButton.sizePolicy().hasHeightForWidth())
        self.ctrlaButton.setSizePolicy(sizePolicy2)
        self.ctrlaButton.setMaximumSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.ctrlaButton, 0, 0, 1, 1)

        self.ctrlbButton = QPushButton(self.groupBox)
        self.ctrlbButton.setObjectName(u"ctrlbButton")
        sizePolicy2.setHeightForWidth(self.ctrlbButton.sizePolicy().hasHeightForWidth())
        self.ctrlbButton.setSizePolicy(sizePolicy2)
        self.ctrlbButton.setMinimumSize(QSize(10, 0))
        self.ctrlbButton.setMaximumSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.ctrlbButton, 0, 1, 1, 1)

        self.ctrleButton = QPushButton(self.groupBox)
        self.ctrleButton.setObjectName(u"ctrleButton")
        sizePolicy2.setHeightForWidth(self.ctrleButton.sizePolicy().hasHeightForWidth())
        self.ctrleButton.setSizePolicy(sizePolicy2)
        self.ctrleButton.setMaximumSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.ctrleButton, 1, 1, 1, 1)

        self.ctrlcButton = QPushButton(self.groupBox)
        self.ctrlcButton.setObjectName(u"ctrlcButton")
        sizePolicy2.setHeightForWidth(self.ctrlcButton.sizePolicy().hasHeightForWidth())
        self.ctrlcButton.setSizePolicy(sizePolicy2)
        self.ctrlcButton.setMaximumSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.ctrlcButton, 0, 2, 1, 1)

        self.ctrldButton = QPushButton(self.groupBox)
        self.ctrldButton.setObjectName(u"ctrldButton")
        sizePolicy2.setHeightForWidth(self.ctrldButton.sizePolicy().hasHeightForWidth())
        self.ctrldButton.setSizePolicy(sizePolicy2)
        self.ctrldButton.setMaximumSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.ctrldButton, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(TerminalDialog)

        QMetaObject.connectSlotsByName(TerminalDialog)
    # setupUi

    def retranslateUi(self, TerminalDialog):
        TerminalDialog.setWindowTitle(QCoreApplication.translate("TerminalDialog", u"Terminal", None))
        self.autoscrollCheckBox.setText(QCoreApplication.translate("TerminalDialog", u"Autoscroll", None))
        self.clearButton.setText(QCoreApplication.translate("TerminalDialog", u"Clear", None))
        self.sendButton.setText(QCoreApplication.translate("TerminalDialog", u"Send", None))
        self.groupBox.setTitle(QCoreApplication.translate("TerminalDialog", u"Control", None))
        self.ctrlaButton.setText(QCoreApplication.translate("TerminalDialog", u"-A", None))
        self.ctrlbButton.setText(QCoreApplication.translate("TerminalDialog", u"-B", None))
        self.ctrleButton.setText(QCoreApplication.translate("TerminalDialog", u"-E", None))
        self.ctrlcButton.setText(QCoreApplication.translate("TerminalDialog", u"-C", None))
        self.ctrldButton.setText(QCoreApplication.translate("TerminalDialog", u"-D", None))
    # retranslateUi

