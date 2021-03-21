# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:04:01 2021

@author: core i5
"""

import AppMenu as am
import sqlite3 as sql3
import sys
from PyQt5.QtWidgets import (QMessageBox, QPushButton, QApplication, QWidget, 
                             QLineEdit, QDesktopWidget, QLabel, QListWidget,
                             QVBoxLayout, QListWidgetItem, QFileDialog)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class registerEmployee(QWidget):
    def __init__(self):
        super().__init__() #initializes the main window
        self.title = "Employee Registration System"
        self.empPhoto = '' #picture column of table customers will have no string unless user uploads picture
        self.x = 100
        self.y = 30
        self.width = 400
        self.height = 400
        self.textboxes()
        self.submit_clear_back()
        self.textboxlabels()
        self.initUI()

        #self.submitbutton.clicked.connect(self.submitfunction)
    
    def textboxes(self):
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(self.x,self.y)
        self.textbox1.resize(100,15)
        
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(self.x,self.y+40)
        self.textbox2.resize(100,15)
        
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(self.x,self.y+80)
        self.textbox3.resize(100,15)
        
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(self.x,self.y+120)
        self.textbox4.resize(100,15)
        
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(self.x,self.y+160)
        self.textbox5.resize(100,15)
        
        self.textbox6 = QLineEdit(self)
        self.textbox6.move(self.x,self.y+200)
        self.textbox6.resize(100,15)
        
        self.textbox7 = QLineEdit(self)
        self.textbox7.move(self.x,self.y+240)
        self.textbox7.resize(100,15)
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.setWindowIcon(QIcon("python.ico"))
        self.center()
        self.show()
        
    def submit_clear_back(self):
        self.submit = QPushButton("Submit", self)
        self.submit.setToolTip("Press to enter selections!")
        self.submit.move(self.x+30,self.y+300)
        self.submit.clicked.connect(self.submit_clicked)

        self.clear = QPushButton("Clear", self)
        self.clear.setToolTip("Press to clear selections!")
        self.clear.move(self.x+120,self.y+300)
        self.clear.clicked.connect(self.clear_clicked)
        
        self.back = QPushButton("Back", self)
        self.back.setToolTip("Press to enter previous page!")
        self.back.move(self.x+75,self.y+335)
        self.back.clicked.connect(self.back_page)
        
        self.submitPhoto = QPushButton("Photo", self)
        self.submitPhoto.setToolTip("Press to submit photo!")
        self.submitPhoto.move(self.x+175,self.y-3)
        self.submitPhoto.clicked.connect(self.open)
    
    def convertToBinaryData(self, filename_):
        #Convert digital data to binary format
        with open(filename_, 'rb') as file:
            blobData = file.read()
        return blobData
    
    
    def open(self):
        self.fileName = QFileDialog.getOpenFileName(self, 'OpenFile')
        print(self.fileName)
        self.insertBLOB(self.fileName)
        
    def insertBLOB(self, photo):
        
        try:
            print("converting image to binary....")
            self.empPhoto = self.convertToBinaryData(photo[0])
            self.textboxlbl7.setStyleSheet('color: red;') 
            print("finished converting....")
        except:
            pass
            
    def clear_clicked(self):
        
        self.textbox2.clear()
        self.textbox3.clear()
        self.textbox4.clear()
        self.textbox5.clear()
        self.textbox6.clear()
        self.textbox7.clear()
        self.textbox1.clear()
        
    def submit_clicked(self):
        
        firstName = self.textbox1.text()
        lastName = self.textbox2.text()
        age = self.textbox3.text()
        job = self.textbox4.text()
        salary = self.textbox5.text()
        email = self.textbox6.text()
        phone = self.textbox7.text()
        cb = sql3.connect('customerDB.db')
        cur = cb.cursor()
        cur.execute("INSERT INTO customers(firstName,lastName, age, job, salary, email, phone, picture) VALUES (?,?,?,?,?,?,?,?)", (firstName,lastName,age,job,salary,email,phone,self.empPhoto))
        cb.commit()
        cb.close()
        self.clear_clicked()
        QMessageBox.information(self,"ALERT","Customer Created!")
        self.empPhoto = ''
        self.textboxlbl7.setStyleSheet('color: black;')
        

    def back_page(self):
        self.dialog = am.appMenu()
        self.dialog.show()
        self.close()
        
    def textboxlabels(self):
                
        self.textboxlbl1 = QLabel("First Name", self)
        self.textboxlbl1.move(self.x-90, self.y+1)
        
        self.textboxlbl2 = QLabel("Last Name", self)
        self.textboxlbl2.move(self.x-90, self.y+41)
        
        self.textboxlbl3 = QLabel("Age", self)
        self.textboxlbl3.move(self.x-90, self.y+81)
        
        self.textboxlbl4 = QLabel("Job", self)
        self.textboxlbl4.move(self.x-90, self.y+121)
        
        self.textboxlbl5 = QLabel("Salary", self)
        self.textboxlbl5.move(self.x-90, self.y+161)
        
        self.textboxlbl6 = QLabel("Email", self)
        self.textboxlbl6.move(self.x-90, self.y+201)
     
        self.textboxlbl6 = QLabel("Phone", self)
        self.textboxlbl6.move(self.x-90, self.y+241)
        
        self.textboxlbl7 = QLabel("Photo", self)
        self.textboxlbl7.move(self.x+130, self.y+1)
        
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
    main = registerEmployee()
    sys.exit(app.exec_())
'''

# Code below creates the database for the customers
'''
cb = sql3.connect('customerDB.db')
try:
    cur = cb.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customers"+
                "(userId INTEGER PRIMARY KEY AUTOINCREMENT,firstName TEXT,lastName TEXT,"+
                "age INTEGER, job TEXT, salary FLOAT, email TEXT, phone TEXT)")
    print("Table successfully created")
    
except:
     print("error in Table creation")
     db.rollback()

cb.close()
'''