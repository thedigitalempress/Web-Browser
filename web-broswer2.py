#!/usr/bin/env python
 
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
 
app = QApplication(sys.argv)
 
web = QWebView()
web.load(QUrl("https://pythonspot.com"))
web.show()
 
sys.exit(app.exec_())
