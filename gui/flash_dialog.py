# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flash_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_FlashDialog(object):
    def setupUi(self, FlashDialog):
        if not FlashDialog.objectName():
            FlashDialog.setObjectName(u"FlashDialog")
        FlashDialog.resize(571, 426)
        self.verticalLayout = QVBoxLayout(FlashDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(FlashDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(80, 0))
        self.label.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.pythonPathEdit = QLineEdit(FlashDialog)
        self.pythonPathEdit.setObjectName(u"pythonPathEdit")
        self.pythonPathEdit.setReadOnly(False)

        self.horizontalLayout.addWidget(self.pythonPathEdit)

        self.pickPythonButton = QPushButton(FlashDialog)
        self.pickPythonButton.setObjectName(u"pickPythonButton")
        self.pickPythonButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.pickPythonButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(FlashDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(80, 0))
        self.label_2.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.firmwarePathEdit = QLineEdit(FlashDialog)
        self.firmwarePathEdit.setObjectName(u"firmwarePathEdit")
        self.firmwarePathEdit.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.firmwarePathEdit)

        self.pickFirmwareButton = QPushButton(FlashDialog)
        self.pickFirmwareButton.setObjectName(u"pickFirmwareButton")
        self.pickFirmwareButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.pickFirmwareButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_4 = QLabel(FlashDialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.portComboBox = QComboBox(FlashDialog)
        self.portComboBox.setObjectName(u"portComboBox")
        self.portComboBox.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.portComboBox)

        self.refreshButton = QPushButton(FlashDialog)
        self.refreshButton.setObjectName(u"refreshButton")
        icon = QIcon()
        icon.addFile(u"icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.refreshButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.wiringButton = QPushButton(FlashDialog)
        self.wiringButton.setObjectName(u"wiringButton")
        self.wiringButton.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_4.addWidget(self.wiringButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_3 = QLabel(FlashDialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.outputEdit = QPlainTextEdit(FlashDialog)
        self.outputEdit.setObjectName(u"outputEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.outputEdit.sizePolicy().hasHeightForWidth())
        self.outputEdit.setSizePolicy(sizePolicy2)
        self.outputEdit.setMinimumSize(QSize(400, 0))
        self.outputEdit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.outputEdit.setFrameShape(QFrame.StyledPanel)
        self.outputEdit.setFrameShadow(QFrame.Sunken)
        self.outputEdit.setLineWidth(1)
        self.outputEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.outputEdit.setUndoRedoEnabled(False)
        self.outputEdit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.outputEdit.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.outputEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.eraseButton = QPushButton(FlashDialog)
        self.eraseButton.setObjectName(u"eraseButton")

        self.horizontalLayout_3.addWidget(self.eraseButton)

        self.flashButton = QPushButton(FlashDialog)
        self.flashButton.setObjectName(u"flashButton")

        self.horizontalLayout_3.addWidget(self.flashButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(FlashDialog)

        QMetaObject.connectSlotsByName(FlashDialog)
    # setupUi

    def retranslateUi(self, FlashDialog):
        FlashDialog.setWindowTitle(QCoreApplication.translate("FlashDialog", u"Flash Firmware", None))
        self.label.setText(QCoreApplication.translate("FlashDialog", u"Python2 path", None))
        self.pickPythonButton.setText(QCoreApplication.translate("FlashDialog", u"Pick", None))
        self.label_2.setText(QCoreApplication.translate("FlashDialog", u"Firmware file", None))
        self.pickFirmwareButton.setText(QCoreApplication.translate("FlashDialog", u"Pick", None))
        self.label_4.setText(QCoreApplication.translate("FlashDialog", u"Port", None))
        self.refreshButton.setText("")
        self.wiringButton.setText(QCoreApplication.translate("FlashDialog", u"Wiring instructions", None))
        self.label_3.setText(QCoreApplication.translate("FlashDialog", u"Flasher output:", None))
        self.eraseButton.setText(QCoreApplication.translate("FlashDialog", u"Erase", None))
        self.flashButton.setText(QCoreApplication.translate("FlashDialog", u"Flash", None))
    # retranslateUi

