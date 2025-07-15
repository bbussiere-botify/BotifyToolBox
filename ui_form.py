# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 708)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pushButton_open = QPushButton(self.tab)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setGeometry(QRect(10, 10, 221, 29))
        self.labelFilename = QLabel(self.tab)
        self.labelFilename.setObjectName(u"labelFilename")
        self.labelFilename.setGeometry(QRect(20, 240, 811, 16))
        self.pushButton_query = QPushButton(self.tab)
        self.pushButton_query.setObjectName(u"pushButton_query")
        self.pushButton_query.setGeometry(QRect(680, 50, 141, 24))
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 40, 651, 51))
        self.textEdit_2 = QTextEdit(self.tab)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 150, 361, 51))
        self.pushButton_keyword = QPushButton(self.tab)
        self.pushButton_keyword.setObjectName(u"pushButton_keyword")
        self.pushButton_keyword.setGeometry(QRect(380, 150, 151, 24))
        self.radioButton_csv = QRadioButton(self.tab)
        self.radioButton_csv.setObjectName(u"radioButton_csv")
        self.radioButton_csv.setGeometry(QRect(540, 150, 111, 20))
        self.radioButton_csv.setChecked(True)
        self.radioButton_cloud = QRadioButton(self.tab)
        self.radioButton_cloud.setObjectName(u"radioButton_cloud")
        self.radioButton_cloud.setGeometry(QRect(670, 150, 161, 20))
        self.comboBox_language = QComboBox(self.tab)
        self.comboBox_language.addItem("")
        self.comboBox_language.addItem("")
        self.comboBox_language.addItem("")
        self.comboBox_language.addItem("")
        self.comboBox_language.addItem("")
        self.comboBox_language.setObjectName(u"comboBox_language")
        self.comboBox_language.setGeometry(QRect(580, 180, 81, 22))
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(380, 180, 191, 31))
        self.pushButton_open_2 = QPushButton(self.tab)
        self.pushButton_open_2.setObjectName(u"pushButton_open_2")
        self.pushButton_open_2.setGeometry(QRect(10, 120, 221, 29))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayout = QFormLayout(self.tab_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEditURL = QLineEdit(self.tab_2)
        self.lineEditURL.setObjectName(u"lineEditURL")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditURL)

        self.pushButton_GoURL = QPushButton(self.tab_2)
        self.pushButton_GoURL.setObjectName(u"pushButton_GoURL")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pushButton_GoURL)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)

        self.formLayout.setLayout(2, QFormLayout.SpanningRole, self.verticalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lineEdit_sitemap = QLineEdit(self.tab_3)
        self.lineEdit_sitemap.setObjectName(u"lineEdit_sitemap")
        self.lineEdit_sitemap.setGeometry(QRect(90, 150, 651, 22))
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 150, 131, 16))
        self.pushButton_sitemap = QPushButton(self.tab_3)
        self.pushButton_sitemap.setObjectName(u"pushButton_sitemap")
        self.pushButton_sitemap.setGeometry(QRect(760, 150, 75, 24))
        self.textEdit_3 = QTextEdit(self.tab_3)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(20, 20, 801, 71))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.plainTextEdit_rules = QPlainTextEdit(self.tab_4)
        self.plainTextEdit_rules.setObjectName(u"plainTextEdit_rules")
        self.plainTextEdit_rules.setGeometry(QRect(70, 50, 751, 101))
        font = QFont()
        font.setFamilies([u"Lucida Console"])
        self.plainTextEdit_rules.setFont(font)
        self.comboBox_ua = QComboBox(self.tab_4)
        self.comboBox_ua.addItem("")
        self.comboBox_ua.addItem("")
        self.comboBox_ua.addItem("")
        self.comboBox_ua.setObjectName(u"comboBox_ua")
        self.comboBox_ua.setGeometry(QRect(490, 10, 331, 26))
        self.label_4 = QLabel(self.tab_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 10, 49, 16))
        self.pushButton_retrieve_robots = QPushButton(self.tab_4)
        self.pushButton_retrieve_robots.setObjectName(u"pushButton_retrieve_robots")
        self.pushButton_retrieve_robots.setGeometry(QRect(390, 10, 75, 24))
        self.lineEdit_rob = QLineEdit(self.tab_4)
        self.lineEdit_rob.setObjectName(u"lineEdit_rob")
        self.lineEdit_rob.setGeometry(QRect(80, 10, 301, 22))
        self.label_5 = QLabel(self.tab_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 10, 81, 16))
        self.plainTextEdit_urls = QPlainTextEdit(self.tab_4)
        self.plainTextEdit_urls.setObjectName(u"plainTextEdit_urls")
        self.plainTextEdit_urls.setGeometry(QRect(70, 160, 751, 101))
        self.label_6 = QLabel(self.tab_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 80, 49, 16))
        self.label_7 = QLabel(self.tab_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 190, 49, 16))
        self.pushButton_check_robots = QPushButton(self.tab_4)
        self.pushButton_check_robots.setObjectName(u"pushButton_check_robots")
        self.pushButton_check_robots.setGeometry(QRect(70, 260, 751, 24))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.lineEdit_burl = QLineEdit(self.tab_5)
        self.lineEdit_burl.setObjectName(u"lineEdit_burl")
        self.lineEdit_burl.setGeometry(QRect(150, 260, 541, 22))
        self.label_8 = QLabel(self.tab_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 260, 121, 16))
        self.pushButton_json = QPushButton(self.tab_5)
        self.pushButton_json.setObjectName(u"pushButton_json")
        self.pushButton_json.setGeometry(QRect(720, 260, 75, 24))
        self.label_9 = QLabel(self.tab_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 100, 81, 16))
        self.pushButton_json_validate = QPushButton(self.tab_5)
        self.pushButton_json_validate.setObjectName(u"pushButton_json_validate")
        self.pushButton_json_validate.setGeometry(QRect(740, 90, 91, 71))
        self.plainTextEdit_json = QPlainTextEdit(self.tab_5)
        self.plainTextEdit_json.setObjectName(u"plainTextEdit_json")
        self.plainTextEdit_json.setGeometry(QRect(90, 20, 631, 201))
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.textBrowserOutput = QTextBrowser(self.centralwidget)
        self.textBrowserOutput.setObjectName(u"textBrowserOutput")

        self.verticalLayout.addWidget(self.textBrowserOutput)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 870, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"Open your SC/BLA Export File", None))
        self.labelFilename.setText(QCoreApplication.translate("MainWindow", u"Selected file", None))
        self.pushButton_query.setText(QCoreApplication.translate("MainWindow", u"Get Top Query Parameter", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Go to <span style=\" font-weight:700;\">SiteCrawler</span> or <span style=\" font-weight:700;\">Log Analyzer</span> and export URLs containing query parameters</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Suggested filter: URL Query match regex .+</p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Go to <span style=\" font-weight:700;\">Keywords Explorer</span> and choose Keyword, Impressions, and Clicks as columns (the default view)</p></body></html>", None))
        self.pushButton_keyword.setText(QCoreApplication.translate("MainWindow", u"Get Top unique Keyword", None))
        self.radioButton_csv.setText(QCoreApplication.translate("MainWindow", u"In the Window", None))
        self.radioButton_cloud.setText(QCoreApplication.translate("MainWindow", u"TagClouds (limited to 100)", None))
        self.comboBox_language.setItemText(0, QCoreApplication.translate("MainWindow", u"english", None))
        self.comboBox_language.setItemText(1, QCoreApplication.translate("MainWindow", u"french", None))
        self.comboBox_language.setItemText(2, QCoreApplication.translate("MainWindow", u"german", None))
        self.comboBox_language.setItemText(3, QCoreApplication.translate("MainWindow", u"italian", None))
        self.comboBox_language.setItemText(4, QCoreApplication.translate("MainWindow", u"spanish", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Language for removing stop words", None))
        self.pushButton_open_2.setText(QCoreApplication.translate("MainWindow", u"Open your RK Export File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Botify", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.pushButton_GoURL.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"PageWorkers", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sitemaps URL", None))
        self.pushButton_sitemap.setText(QCoreApplication.translate("MainWindow", u"Retrieve", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Extract all URLs present in the sitemap.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If hreflang is present add columns with the link between the url and language</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Sitemap", None))
        self.comboBox_ua.setItemText(0, QCoreApplication.translate("MainWindow", u"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0)", None))
        self.comboBox_ua.setItemText(1, QCoreApplication.translate("MainWindow", u"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36", None))
        self.comboBox_ua.setItemText(2, QCoreApplication.translate("MainWindow", u"Mozilla/5.0 (compatible; botify; http://botify.com)", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"UA", None))
        self.pushButton_retrieve_robots.setText(QCoreApplication.translate("MainWindow", u"Retrieve", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Robots.txt URL", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Rules", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"URLs", None))
        self.pushButton_check_robots.setText(QCoreApplication.translate("MainWindow", u"Check URLs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Robots.txt", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Botify's URL with filter", None))
        self.pushButton_json.setText(QCoreApplication.translate("MainWindow", u"Get JSON", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"JSON input", None))
        self.pushButton_json_validate.setText(QCoreApplication.translate("MainWindow", u"Validate \n"
" and \n"
"Make beautiful", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"JSON", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"API", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

