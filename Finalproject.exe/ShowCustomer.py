# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:28:02 2021

@author: core i5
"""
import SearchCustomer as searchC
import sqlite3 as sql3
import sys
from PyQt5.QtWidgets import (QMessageBox, QPushButton, QApplication, QWidget, 
                             QLineEdit, QDesktopWidget, QLabel, QListWidget,
                             QVBoxLayout, QListWidgetItem, QFileDialog)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class showEmployee(QWidget):
    def __init__(self, data):
        super().__init__() #initializes the main window
        self.title = "Employee Profile"
        self.empPhoto = '' #picture column of table customers will have no string unless user uploads picture
        self.x = 100
        self.y = 200
        self.width = 400
        self.height = 400
        self.getCustomer(data)
        self.textboxlabels()
        self.back()
        self.initUI()
        #self.submitbutton.clicked.connect(self.submitfunction)
    
    def getCustomer(self, data):
        self.dataC = data
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.setWindowIcon(QIcon("python.ico"))
        self.center()
        self.show()
        
    def back(self): 
        
        self.back = QPushButton("Back", self)
        self.back.setToolTip("Press to enter previous page!")
        self.back.move(self.x+75,self.y+145)
        self.back.clicked.connect(self.back_page)      
          
    def back_page(self):
        self.dialog = searchC.searchCustomer()
        self.dialog.show()
        self.close()
        
    def textboxlabels(self):
                
        self.textboxlbl1 = QLabel(f"First Name: \t{self.dataC[0]}", self)
        self.textboxlbl1.move(self.x-90, self.y+1)
        
        self.textboxlbl2 = QLabel(f"Last Name: \t{self.dataC[1]}", self)
        self.textboxlbl2.move(self.x-90, self.y+21)
        
        self.textboxlbl3 = QLabel(f"Age: \t\t{self.dataC[2]}", self)
        self.textboxlbl3.move(self.x-90, self.y+41)
        
        self.textboxlbl4 = QLabel(f"Job: \t\t{self.dataC[3]}", self)
        self.textboxlbl4.move(self.x-90, self.y+61)
        
        self.textboxlbl5 = QLabel(f"Salary: \t\t{self.dataC[4]}", self)
        self.textboxlbl5.move(self.x-90, self.y+81)
        
        self.textboxlbl6 = QLabel(f"Email: \t\t{self.dataC[5]}", self)
        self.textboxlbl6.move(self.x-90, self.y+101)
     
        self.textboxlbl6 = QLabel(f"Phone: \t\t{self.dataC[6]}", self)
        self.textboxlbl6.move(self.x-90, self.y+121)
        
        #self.textboxlbl7 = QLabel("Photo", self)
        #self.textboxlbl7.move(self.x+130, self.y+1)
        
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
    main = showEmployee()
    sys.exit(app.exec_())
'''