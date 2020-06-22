# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MovieSource.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from MovieSpider import *

class Ui_MovieSource(object):
    def setupUi(self, MovieSource):
        MovieSource.setObjectName("MovieSource")
        MovieSource.resize(360, 301)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MovieSource.setWindowIcon(icon)
        MovieSource.setStyleSheet("#MovieSource{\n"
"border-image:url(:/pic/背景图片.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MovieSource)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MovieName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华光准圆_CNKI")
        self.MovieName.setFont(font)
        self.MovieName.setObjectName("MovieName")
        self.horizontalLayout.addWidget(self.MovieName)
        self.MovieInput = QtWidgets.QLineEdit(self.centralwidget)
        self.MovieInput.setStyleSheet("#MovieInput{\n"
"background:transparent;\n"
"}")
        self.MovieInput.setClearButtonEnabled(True)
        self.MovieInput.setObjectName("MovieInput")
        self.horizontalLayout.addWidget(self.MovieInput)
        self.SourceName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华光准圆_CNKI")
        self.SourceName.setFont(font)
        self.SourceName.setObjectName("SourceName")
        self.horizontalLayout.addWidget(self.SourceName)
        self.Source_cbBox = QtWidgets.QComboBox(self.centralwidget)
        self.Source_cbBox.setStyleSheet("#Source_cbBox{\n"
"background:transparent;\n"
"}")
        self.Source_cbBox.setObjectName("Source_cbBox")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/热度.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Source_cbBox.addItem(icon1, "")
        self.horizontalLayout.addWidget(self.Source_cbBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StateLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华光准圆_CNKI")
        self.StateLabel.setFont(font)
        self.StateLabel.setObjectName("StateLabel")
        self.horizontalLayout_2.addWidget(self.StateLabel)
        self.State = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华光准圆_CNKI")
        self.State.setFont(font)
        self.State.setObjectName("State")
        self.horizontalLayout_2.addWidget(self.State)
        spacerItem = QtWidgets.QSpacerItem(168, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SearchButton.setStyleSheet("#SearchButton{\n"
"background:transparent;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pic/搜索.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon2)
        self.SearchButton.setObjectName("SearchButton")
        self.horizontalLayout_2.addWidget(self.SearchButton)
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet("#CloseButton{\n"
"background:transparent\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CloseButton.setIcon(icon3)
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout_2.addWidget(self.CloseButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.MovieList = QtWidgets.QListWidget(self.centralwidget)
        self.MovieList.setStyleSheet("#MovieList{\n"
"background:transparent;\n"
"}")
        self.MovieList.setObjectName("MovieList")
        self.verticalLayout.addWidget(self.MovieList)
        MovieSource.setCentralWidget(self.centralwidget)

        self.spider = MovieSpider(self)
        self.SearchButton.clicked.connect(self.search)
        self.MovieList.itemDoubleClicked.connect(self.spider.clip_url)
        self.CloseButton.clicked.connect(self.terminal)

        self.retranslateUi(MovieSource)
        QtCore.QMetaObject.connectSlotsByName(MovieSource)

    def retranslateUi(self, MovieSource):
        _translate = QtCore.QCoreApplication.translate
        MovieSource.setWindowTitle(_translate("MovieSource", "电影资源搜索"))
        self.MovieName.setText(_translate("MovieSource", "电影名称:"))
        self.SourceName.setText(_translate("MovieSource", "选择片源:"))
        self.Source_cbBox.setItemText(0, _translate("MovieSource", "电影天堂"))
        self.StateLabel.setText(_translate("MovieSource", "查询状态:"))
        self.State.setText(_translate("MovieSource", "未开始查询"))
        self.SearchButton.setText(_translate("MovieSource", "查询"))
        self.CloseButton.setText(_translate("MovieSource", "停止搜索"))

    def search(self):
        self.spider.terminate()
        self.spider.wait()
        self.spider.start()

    def terminal(self):
        self.spider.terminate()
        self.spider.wait()
        self.State.setText('查找中止.')
import source_rc