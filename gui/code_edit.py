# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'code_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_CodeEditDialog(object):
    def setupUi(self, CodeEditDialog):
        if not CodeEditDialog.objectName():
            CodeEditDialog.setObjectName(u"CodeEditDialog")
        CodeEditDialog.resize(954, 537)
        self.verticalLayout = QVBoxLayout(CodeEditDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_4 = QLabel(CodeEditDialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.label_7 = QLabel(CodeEditDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(40, 0))

        self.horizontalLayout.addWidget(self.label_7)

        self.localPathEdit = QLineEdit(CodeEditDialog)
        self.localPathEdit.setObjectName(u"localPathEdit")

        self.horizontalLayout.addWidget(self.localPathEdit)

        self.saveLocalButton = QPushButton(CodeEditDialog)
        self.saveLocalButton.setObjectName(u"saveLocalButton")
        self.saveLocalButton.setMaximumSize(QSize(70, 16777215))
        icon = QIcon()
        icon.addFile(u"icons/floppy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveLocalButton.setIcon(icon)
        self.saveLocalButton.setIconSize(QSize(20, 20))
        self.saveLocalButton.setFlat(False)

        self.horizontalLayout.addWidget(self.saveLocalButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.label_8 = QLabel(CodeEditDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_2.addWidget(self.label_8)

        self.remotePathEdit = QLineEdit(CodeEditDialog)
        self.remotePathEdit.setObjectName(u"remotePathEdit")

        self.horizontalLayout_2.addWidget(self.remotePathEdit)

        self.runButton = QPushButton(CodeEditDialog)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setMinimumSize(QSize(0, 0))
        self.runButton.setMaximumSize(QSize(60, 16777215))
        icon1 = QIcon()
        icon1.addFile(u"icons/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.runButton.setIcon(icon1)
        self.runButton.setIconSize(QSize(20, 20))
        self.runButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.runButton)

        self.saveMcuButton = QPushButton(CodeEditDialog)
        self.saveMcuButton.setObjectName(u"saveMcuButton")
        self.saveMcuButton.setMaximumSize(QSize(70, 16777215))
        self.saveMcuButton.setIcon(icon)
        self.saveMcuButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.saveMcuButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.codeEdit = QTextEdit(CodeEditDialog)
        self.codeEdit.setObjectName(u"codeEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.codeEdit.sizePolicy().hasHeightForWidth())
        self.codeEdit.setSizePolicy(sizePolicy)
        self.codeEdit.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout.addWidget(self.codeEdit)


        self.retranslateUi(CodeEditDialog)

        QMetaObject.connectSlotsByName(CodeEditDialog)
    # setupUi

    def retranslateUi(self, CodeEditDialog):
        CodeEditDialog.setWindowTitle(QCoreApplication.translate("CodeEditDialog", u"Code Editor", None))
        self.label_4.setText(QCoreApplication.translate("CodeEditDialog", u"Filename:", None))
        self.label_7.setText(QCoreApplication.translate("CodeEditDialog", u"Local", None))
        self.saveLocalButton.setText(QCoreApplication.translate("CodeEditDialog", u"Save", None))
        self.label_8.setText(QCoreApplication.translate("CodeEditDialog", u"MCU", None))
        self.runButton.setText(QCoreApplication.translate("CodeEditDialog", u"Run", None))
        self.saveMcuButton.setText(QCoreApplication.translate("CodeEditDialog", u"Save", None))
    # retranslateUi

