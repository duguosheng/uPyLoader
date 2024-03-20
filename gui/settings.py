# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(706, 503)
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.editorGroupBox = QGroupBox(SettingsDialog)
        self.editorGroupBox.setObjectName(u"editorGroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.editorGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.editorFormLayout = QFormLayout()
        self.editorFormLayout.setObjectName(u"editorFormLayout")
        self.label_4 = QLabel(self.editorGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.editorFormLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.editorGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.editorFormLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.externalCommandLineEdit = QLineEdit(self.editorGroupBox)
        self.externalCommandLineEdit.setObjectName(u"externalCommandLineEdit")

        self.editorFormLayout.setWidget(1, QFormLayout.FieldRole, self.externalCommandLineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.externalPathLineEdit = QLineEdit(self.editorGroupBox)
        self.externalPathLineEdit.setObjectName(u"externalPathLineEdit")

        self.horizontalLayout.addWidget(self.externalPathLineEdit)

        self.externalPathBrowseButton = QPushButton(self.editorGroupBox)
        self.externalPathBrowseButton.setObjectName(u"externalPathBrowseButton")
        self.externalPathBrowseButton.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.externalPathBrowseButton)


        self.editorFormLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.editorFormLayout)


        self.verticalLayout.addWidget(self.editorGroupBox)

        self.terminalGroupBox = QGroupBox(SettingsDialog)
        self.terminalGroupBox.setObjectName(u"terminalGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.terminalGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.terminalFormLayout = QFormLayout()
        self.terminalFormLayout.setObjectName(u"terminalFormLayout")
        self.label = QLabel(self.terminalGroupBox)
        self.label.setObjectName(u"label")

        self.terminalFormLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.newLineKeyEdit = QLineEdit(self.terminalGroupBox)
        self.newLineKeyEdit.setObjectName(u"newLineKeyEdit")

        self.terminalFormLayout.setWidget(0, QFormLayout.FieldRole, self.newLineKeyEdit)

        self.label_2 = QLabel(self.terminalGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.terminalFormLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.sendKeyEdit = QLineEdit(self.terminalGroupBox)
        self.sendKeyEdit.setObjectName(u"sendKeyEdit")

        self.terminalFormLayout.setWidget(1, QFormLayout.FieldRole, self.sendKeyEdit)

        self.label_6 = QLabel(self.terminalGroupBox)
        self.label_6.setObjectName(u"label_6")

        self.terminalFormLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.tabSpacesSpinBox = QSpinBox(self.terminalGroupBox)
        self.tabSpacesSpinBox.setObjectName(u"tabSpacesSpinBox")
        self.tabSpacesSpinBox.setMinimumSize(QSize(50, 0))
        self.tabSpacesSpinBox.setMinimum(1)
        self.tabSpacesSpinBox.setMaximum(8)

        self.horizontalLayout_2.addWidget(self.tabSpacesSpinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.terminalFormLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.terminalFormLayout)


        self.verticalLayout.addWidget(self.terminalGroupBox)

        self.groupBox = QGroupBox(SettingsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.mpyCrossPathLineEdit = QLineEdit(self.groupBox)
        self.mpyCrossPathLineEdit.setObjectName(u"mpyCrossPathLineEdit")

        self.horizontalLayout_3.addWidget(self.mpyCrossPathLineEdit)

        self.mpyPathBrowseButton = QPushButton(self.groupBox)
        self.mpyPathBrowseButton.setObjectName(u"mpyPathBrowseButton")
        self.mpyPathBrowseButton.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.mpyPathBrowseButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(SettingsDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.preferredPortLineEdit = QLineEdit(self.groupBox_2)
        self.preferredPortLineEdit.setObjectName(u"preferredPortLineEdit")
        self.preferredPortLineEdit.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.preferredPortLineEdit)


        self.verticalLayout_5.addLayout(self.formLayout_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(SettingsDialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.useCustomTransferFilesCheckBox = QCheckBox(self.groupBox_3)
        self.useCustomTransferFilesCheckBox.setObjectName(u"useCustomTransferFilesCheckBox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.useCustomTransferFilesCheckBox)

        self.useTransferFilesCheckBox = QCheckBox(self.groupBox_3)
        self.useTransferFilesCheckBox.setObjectName(u"useTransferFilesCheckBox")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.useTransferFilesCheckBox)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.transferFilesPathLineEdit = QLineEdit(self.groupBox_3)
        self.transferFilesPathLineEdit.setObjectName(u"transferFilesPathLineEdit")

        self.horizontalLayout_4.addWidget(self.transferFilesPathLineEdit)

        self.transferFilesPathBrowseButton = QPushButton(self.groupBox_3)
        self.transferFilesPathBrowseButton.setObjectName(u"transferFilesPathBrowseButton")
        self.transferFilesPathBrowseButton.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.transferFilesPathBrowseButton)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.verticalLayout_6.addLayout(self.formLayout_3)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.editorGroupBox.setTitle(QCoreApplication.translate("SettingsDialog", u"Editor", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"Path to external editor", None))
        self.label_5.setText(QCoreApplication.translate("SettingsDialog", u"External editor arguments", None))
        self.externalPathBrowseButton.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
        self.terminalGroupBox.setTitle(QCoreApplication.translate("SettingsDialog", u"Terminal", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"New line key", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Send key", None))
        self.label_6.setText(QCoreApplication.translate("SettingsDialog", u"Tab spaces", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsDialog", u"Compiler", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"mpy-cross path", None))
        self.mpyPathBrowseButton.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingsDialog", u"Connection", None))
        self.label_7.setText(QCoreApplication.translate("SettingsDialog", u"Preferred port", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SettingsDialog", u"Serial (UART)", None))
        self.label_10.setText(QCoreApplication.translate("SettingsDialog", u"Use transfer files (recommended)", None))
        self.label_9.setText(QCoreApplication.translate("SettingsDialog", u"Use custom transfer files", None))
        self.useCustomTransferFilesCheckBox.setText("")
        self.useTransferFilesCheckBox.setText("")
        self.label_8.setText(QCoreApplication.translate("SettingsDialog", u"Path to custom transfer files", None))
        self.transferFilesPathBrowseButton.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
    # retranslateUi

