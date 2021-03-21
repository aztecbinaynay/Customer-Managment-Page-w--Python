# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 05:40:57 2021

@author: core i5
"""

import LoginPage as lp
import BetaDeletePage as du
import SearchCustomer as searchC
import CreateEmployee as ce
import sqlite3 as sql3
import sys
from PyQt5.QtWidgets import QMessageBox, QPushButton, QApplication, QWidget, QLineEdit, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon, QFont

class appMenu(QWidget): #QWidget is the base class for all GUI elements in the PyQt5.

    def __init__(self):      
        super().__init__() #initializes the main window
        self.title = "Employee Management System Menu"
        self.x = 60
        self.y = 100
        self.width = 400
        self.height = 400
        self.buttons()
        self.mainTitle()
        self.initUI()
    
    def mainTitle(self):
        self.MainTitle = QLabel("Employee Management\n"+7*" "+"System Menu", self)
        self.MainTitle.move(self.x, self.y)
        self.MainTitle.setFont(QFont('Times', 20))
        
    def buttons(self):
        self.create = QPushButton(" Create employee ", self)
        self.create.setToolTip("Press to create employee page!")
        self.create.move(self.x+30,self.y+120)
        self.create.clicked.connect(self.create_clicked)

        self.search = QPushButton(" Search Employee ", self)
        self.search.setToolTip("Press to search employee page!")
        self.search.move(self.x+140,self.y+120)
        self.search.clicked.connect(self.search_clicked)
        
        self.logOut = QPushButton("Log Out", self)
        self.logOut.setToolTip("Press to log out of the system!")
        self.logOut.move(self.x+42,self.y+160)
        self.logOut.clicked.connect(self.logOut_clicked)
        
        self.deleteUser = QPushButton("delete user", self)
        self.deleteUser.setToolTip("Press to delete an admin!")
        self.deleteUser.move(self.x+152,self.y+160)
        self.deleteUser.setStyleSheet('color: red;')
        self.deleteUser.clicked.connect(self.deleteUser_clicked)
    
    def create_clicked(self):
        self.dialog = ce.registerEmployee()
        self.dialog.show()
        self.close()
    
    def search_clicked(self):
        self.dialog = searchC.searchCustomer()
        self.dialog.show()
        self.close()
        
    def logOut_clicked(self):
        self.dialog = lp.loginUser()
        self.dialog.show()
        self.close()
        
    def deleteUser_clicked(self):
        self.dialog = du.deleteUser()
        self.dialog.show()
        self.close()
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.setWindowIcon(QIcon("python.ico"))
        self.center()
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())





'''
    run this code when you need to speecifically see
    this page

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = appMenu()
    sys.exit(app.exec_())
'''