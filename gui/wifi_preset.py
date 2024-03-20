# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wifi_preset.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QListView, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_WiFiPresetDialog(object):
    def setupUi(self, WiFiPresetDialog):
        if not WiFiPresetDialog.objectName():
            WiFiPresetDialog.setObjectName(u"WiFiPresetDialog")
        WiFiPresetDialog.resize(451, 420)
        self.verticalLayout = QVBoxLayout(WiFiPresetDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.presetsListView = QListView(WiFiPresetDialog)
        self.presetsListView.setObjectName(u"presetsListView")
        self.presetsListView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout.addWidget(self.presetsListView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(WiFiPresetDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(70, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.nameLineEdit = QLineEdit(WiFiPresetDialog)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.nameLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(WiFiPresetDialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(70, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.ipLineEdit = QLineEdit(WiFiPresetDialog)
        self.ipLineEdit.setObjectName(u"ipLineEdit")
        self.ipLineEdit.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.ipLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_4 = QLabel(WiFiPresetDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(70, 0))
        self.label_4.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.portSpinBox = QSpinBox(WiFiPresetDialog)
        self.portSpinBox.setObjectName(u"portSpinBox")
        self.portSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.portSpinBox.setMaximum(65536)
        self.portSpinBox.setValue(0)

        self.horizontalLayout_4.addWidget(self.portSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(WiFiPresetDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.passwordLineEdit = QLineEdit(WiFiPresetDialog)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setMinimumSize(QSize(200, 0))
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.passwordLineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.label_5 = QLabel(WiFiPresetDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(Qt.AutoText)

        self.verticalLayout_4.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.addButton = QPushButton(WiFiPresetDialog)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout_3.addWidget(self.addButton)

        self.removeButton = QPushButton(WiFiPresetDialog)
        self.removeButton.setObjectName(u"removeButton")

        self.verticalLayout_3.addWidget(self.removeButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(WiFiPresetDialog)

        QMetaObject.connectSlotsByName(WiFiPresetDialog)
    # setupUi

    def retranslateUi(self, WiFiPresetDialog):
        WiFiPresetDialog.setWindowTitle(QCoreApplication.translate("WiFiPresetDialog", u"Presets", None))
        self.label_2.setText(QCoreApplication.translate("WiFiPresetDialog", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("WiFiPresetDialog", u"IP adress", None))
        self.label_4.setText(QCoreApplication.translate("WiFiPresetDialog", u"Port", None))
        self.label.setText(QCoreApplication.translate("WiFiPresetDialog", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("WiFiPresetDialog", u"<html><head/><body><p><span style=\" color:#d50003;\">Warning: passwords are saved as plaintext</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("WiFiPresetDialog", u"Add", None))
        self.removeButton.setText(QCoreApplication.translate("WiFiPresetDialog", u"Remove", None))
    # retranslateUi

