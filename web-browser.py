import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QtWidgets.QWidget):

    def __init__(self) :
        super(Browser, self).__init__()

        self.webview = QWebEngineView(self)
        self.webview.load(QUrl("http://www.google.com"))
        self.setGeometry(0, 0, 800, 600)

        self.back_btn = QtWidgets.QPushButton("<", self)
        self.back_btn.clicked.connect(self.webview.back)
        self.back_btn.setMaximumSize(20, 20)

        self.forward_btn = QtWidgets.QPushButton(">", self)
        self.forward_btn.clicked.connect(self.webview.forward)
        self.forward_btn.setMaximumSize(20,20)

        self.url_entry = QtWidgets.QLineEdit(self)
        self.url_entry.setMinimumSize(200, 20)
        self.url_entry.setMaximumSize(300, 20)

        self.go_btn = QtWidgets.QPushButton("Go", self)
        self.go_btn.clicked.connect(self.go_btn_clicked)
        self.go_btn.setMaximumSize(30, 20)

        self.favourites = QtWidgets.QComboBox(self)
        self.favourites.addItems(["http://www.google.com",
                                  "http://www.raspberrypi.org",
                                  "http://www.thedigitalempress.tech"])
        self.favourites.activated.connect(self.favourite_selected)
        self.favourites.setMinimumSize(200, 20)
        self.favourites.setMaximumSize(300, 20)

        self.search_box = QtWidgets.QLineEdit(self)
        self.search_box.setMinimumSize(200, 20)
        self.search_box.setMaximumSize(300, 20)

        self.search_btn = QtWidgets.QPushButton("Search", self)
        self.search_btn.clicked.connect(self.search_btn_clicked)
        self.search_btn.setMaximumSize(50, 20)

        self.zoom_slider = QtWidgets.QSlider(Qt.Orientation(1), self)
        self.zoom_slider.setRange(2, 50)
        self.zoom_slider.setValue(10)
        self.zoom_slider.valueChanged.connect(self.zoom_changed)

        self.zoom_label = QtWidgets.QLabel("Zoom:")

        self.webview.loadStarted.connect(self.page_loading)


        self.menu_bar = QtWidgets.QHBoxLayout()
        self.menu_bar.addWidget(self.back_btn)
        self.menu_bar.addWidget(self.forward_btn)
        self.menu_bar.addWidget(self.url_entry)
        self.menu_bar.addWidget(self.go_btn)
        self.menu_bar.addStretch()
        self.menu_bar.addWidget(self.favourites)
        self.menu_bar.addStretch()
        self.menu_bar.addWidget(self.search_box)
        self.menu_bar.addWidget(self.search_btn)
        self.menu_bar.addWidget(self.zoom_slider)


        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.menu_bar)
        self.main_layout.addWidget(self.webview)

        self.setLayout(self.main_layout)

    def go_btn_clicked(self):
        self.webview.load(self.url_entry.text())

    def favourite_selected(self):
        self.webview.load(self.favourites.currentText())

    def zoom_changed(self):
        self.webview.setZoomFactor(self.zoom_slider.value()/10)
        
    def search_btn_clicked(self):
        self.webview.load("https://www.google.com/search?q="
                          + self.search_box.text())

    def page_loading(self):
        self.url_entry.setText(self.webview.url().toString())




class BrowserWindow (QtWidgets.QMainWindow) :
    def __init__(self):
        super(BrowserWindow, self).__init__()
        self.widget = Browser()
        self.setCentralWidget (self.widget)



#Create a QT application
app = QApplication(sys.argv)
window = BrowserWindow ()
window.show()

#Enter Qt application main loop
app.exec_()
sys.exit()
