# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_transfer.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_FileTransferDialog(object):
    def setupUi(self, FileTransferDialog):
        if not FileTransferDialog.objectName():
            FileTransferDialog.setObjectName(u"FileTransferDialog")
        FileTransferDialog.resize(400, 120)
        self.verticalLayout_2 = QVBoxLayout(FileTransferDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(FileTransferDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(FileTransferDialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(FileTransferDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setEnabled(False)
        self.cancelButton.setCheckable(False)

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(FileTransferDialog)

        QMetaObject.connectSlotsByName(FileTransferDialog)
    # setupUi

    def retranslateUi(self, FileTransferDialog):
        FileTransferDialog.setWindowTitle(QCoreApplication.translate("FileTransferDialog", u"File Transfer", None))
        self.label.setText(QCoreApplication.translate("FileTransferDialog", u"TextLabel", None))
        self.cancelButton.setText(QCoreApplication.translate("FileTransferDialog", u"Cancel", None))
    # retranslateUi

