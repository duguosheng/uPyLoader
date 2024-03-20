# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QListView, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

from src.gui.controls.transfer_tree_view import TransferTreeView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 597)
        self.actionNavigate = QAction(MainWindow)
        self.actionNavigate.setObjectName(u"actionNavigate")
        self.actionTerminal = QAction(MainWindow)
        self.actionTerminal.setObjectName(u"actionTerminal")
        self.actionUpload = QAction(MainWindow)
        self.actionUpload.setObjectName(u"actionUpload")
        self.actionCode_Editor = QAction(MainWindow)
        self.actionCode_Editor.setObjectName(u"actionCode_Editor")
        self.actionFlash = QAction(MainWindow)
        self.actionFlash.setObjectName(u"actionFlash")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.horizontalLayout_3.addWidget(self.statusLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.connectionComboBox = QComboBox(self.centralwidget)
        self.connectionComboBox.setObjectName(u"connectionComboBox")
        self.connectionComboBox.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.connectionComboBox)

        self.refreshButton = QPushButton(self.centralwidget)
        self.refreshButton.setObjectName(u"refreshButton")
        icon = QIcon()
        icon.addFile(u"icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.refreshButton)

        self.connectionStackedWidget = QStackedWidget(self.centralwidget)
        self.connectionStackedWidget.setObjectName(u"connectionStackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectionStackedWidget.sizePolicy().hasHeightForWidth())
        self.connectionStackedWidget.setSizePolicy(sizePolicy)
        self.uartPage = QWidget()
        self.uartPage.setObjectName(u"uartPage")
        self.horizontalLayout_5 = QHBoxLayout(self.uartPage)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.uartPage)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.baudComboBox = QComboBox(self.uartPage)
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.setObjectName(u"baudComboBox")

        self.horizontalLayout_5.addWidget(self.baudComboBox)

        self.serialResetCheckBox = QCheckBox(self.uartPage)
        self.serialResetCheckBox.setObjectName(u"serialResetCheckBox")
        self.serialResetCheckBox.setChecked(False)

        self.horizontalLayout_5.addWidget(self.serialResetCheckBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.connectionStackedWidget.addWidget(self.uartPage)
        self.wifiPage = QWidget()
        self.wifiPage.setObjectName(u"wifiPage")
        self.horizontalLayout_6 = QHBoxLayout(self.wifiPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.wifiPage)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.addressLineEdit = QLineEdit(self.wifiPage)
        self.addressLineEdit.setObjectName(u"addressLineEdit")
        self.addressLineEdit.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_6.addWidget(self.addressLineEdit)

        self.label_6 = QLabel(self.wifiPage)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.portSpinBox = QSpinBox(self.wifiPage)
        self.portSpinBox.setObjectName(u"portSpinBox")
        self.portSpinBox.setMaximum(65536)
        self.portSpinBox.setValue(8266)

        self.horizontalLayout_6.addWidget(self.portSpinBox)

        self.presetButton = QPushButton(self.wifiPage)
        self.presetButton.setObjectName(u"presetButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.presetButton.sizePolicy().hasHeightForWidth())
        self.presetButton.setSizePolicy(sizePolicy2)
        self.presetButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_6.addWidget(self.presetButton)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.connectionStackedWidget.addWidget(self.wifiPage)

        self.horizontalLayout_3.addWidget(self.connectionStackedWidget)

        self.connectButton = QPushButton(self.centralwidget)
        self.connectButton.setObjectName(u"connectButton")

        self.horizontalLayout_3.addWidget(self.connectButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy3)
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_7)

        self.localFilesTreeView = TransferTreeView(self.verticalLayoutWidget_2)
        self.localFilesTreeView.setObjectName(u"localFilesTreeView")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.localFilesTreeView.sizePolicy().hasHeightForWidth())
        self.localFilesTreeView.setSizePolicy(sizePolicy4)
        self.localFilesTreeView.setMinimumSize(QSize(250, 0))
        self.localFilesTreeView.setMaximumSize(QSize(16777215, 16777215))
        self.localFilesTreeView.setBaseSize(QSize(0, 0))
        self.localFilesTreeView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.localFilesTreeView.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.localFilesTreeView)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.compileButton = QPushButton(self.verticalLayoutWidget_2)
        self.compileButton.setObjectName(u"compileButton")

        self.horizontalLayout_7.addWidget(self.compileButton)

        self.autoTransferCheckBox = QCheckBox(self.verticalLayoutWidget_2)
        self.autoTransferCheckBox.setObjectName(u"autoTransferCheckBox")
        self.autoTransferCheckBox.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_7.addWidget(self.autoTransferCheckBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.remoteNameEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.remoteNameEdit.setObjectName(u"remoteNameEdit")

        self.horizontalLayout_4.addWidget(self.remoteNameEdit)

        self.transferToMcuButton = QPushButton(self.verticalLayoutWidget_2)
        self.transferToMcuButton.setObjectName(u"transferToMcuButton")
        self.transferToMcuButton.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_4.addWidget(self.transferToMcuButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.splitter.addWidget(self.verticalLayoutWidget_2)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.mcuFilesListView = QListView(self.verticalLayoutWidget)
        self.mcuFilesListView.setObjectName(u"mcuFilesListView")
        sizePolicy4.setHeightForWidth(self.mcuFilesListView.sizePolicy().hasHeightForWidth())
        self.mcuFilesListView.setSizePolicy(sizePolicy4)
        self.mcuFilesListView.setMinimumSize(QSize(150, 0))
        self.mcuFilesListView.setMaximumSize(QSize(16777215, 16777215))
        self.mcuFilesListView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout.addWidget(self.mcuFilesListView)

        self.listButton = QPushButton(self.verticalLayoutWidget)
        self.listButton.setObjectName(u"listButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.listButton.sizePolicy().hasHeightForWidth())
        self.listButton.setSizePolicy(sizePolicy5)

        self.verticalLayout.addWidget(self.listButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.executeButton = QPushButton(self.verticalLayoutWidget)
        self.executeButton.setObjectName(u"executeButton")

        self.horizontalLayout.addWidget(self.executeButton)

        self.removeButton = QPushButton(self.verticalLayoutWidget)
        self.removeButton.setObjectName(u"removeButton")

        self.horizontalLayout.addWidget(self.removeButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.localPathEdit = QLineEdit(self.verticalLayoutWidget)
        self.localPathEdit.setObjectName(u"localPathEdit")

        self.horizontalLayout_2.addWidget(self.localPathEdit)

        self.transferToPcButton = QPushButton(self.verticalLayoutWidget)
        self.transferToPcButton.setObjectName(u"transferToPcButton")
        self.transferToPcButton.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.transferToPcButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.verticalLayoutWidget)

        self.verticalLayout_4.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNavigate)
        self.menuFile.addAction(self.actionUpload)
        self.menuFile.addAction(self.actionFlash)
        self.menuView.addAction(self.actionTerminal)
        self.menuView.addAction(self.actionCode_Editor)
        self.menuOptions.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.connectionStackedWidget.setCurrentIndex(0)
        self.baudComboBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"uPyLoader", None))
        self.actionNavigate.setText(QCoreApplication.translate("MainWindow", u"Navigate", None))
        self.actionTerminal.setText(QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.actionUpload.setText(QCoreApplication.translate("MainWindow", u"Init transfer files", None))
        self.actionCode_Editor.setText(QCoreApplication.translate("MainWindow", u"Code Editor", None))
        self.actionFlash.setText(QCoreApplication.translate("MainWindow", u"Flash firmware", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About uPyLoader", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.refreshButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Baud rate:", None))
        self.baudComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.baudComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"115200", None))

        self.serialResetCheckBox.setText(QCoreApplication.translate("MainWindow", u"Issue reset", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"IP address or domain name", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.addressLineEdit.setText(QCoreApplication.translate("MainWindow", u"192.168.4.1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.presetButton.setText(QCoreApplication.translate("MainWindow", u"preset", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.compileButton.setText(QCoreApplication.translate("MainWindow", u"Compile", None))
        self.autoTransferCheckBox.setText(QCoreApplication.translate("MainWindow", u"Auto-transfer", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"MCU name:", None))
        self.transferToMcuButton.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Remote (MCU)", None))
        self.listButton.setText(QCoreApplication.translate("MainWindow", u"List files", None))
        self.executeButton.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"PC path:", None))
        self.transferToPcButton.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

