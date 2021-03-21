# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 10:28:06 2021

@author: core i5
"""
import AppMenu as ap
import sqlite3 as sql3
import RegistrationPage as rp
import sys
from PyQt5.QtWidgets import QMessageBox, QPushButton, QApplication, QWidget, QLineEdit, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon, QFont

class loginUser(QWidget):
    
    def __init__(self):
        super().__init__() #initializes the main window
        self.title = "Login System"
        self.x = 100
        self.y = 30
        self.width = 400
        self.height = 400
        self.textboxes()
        self.submit_register()
        self.initUI()


        #self.submitbutton.clicked.connect(self.submitfunction)
    
    def textboxes(self):
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(self.x+30,self.y+120)
        self.textbox1.resize(150,15)
        self.textbox1.setPlaceholderText("username")

        
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(self.x+30,self.y+150)
        self.textbox2.resize(150,15)
        self.textbox2.setPlaceholderText("password")
        self.textbox2.setEchoMode(QLineEdit.Password)
    
    def initUI(self):
        self.MainTitle = QLabel("LOGIN PAGE", self)
        self.MainTitle.move(self.x+28, self.y+30)
        self.MainTitle.setFont(QFont('Times', 20))
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.setWindowIcon(QIcon("python.ico"))
        self.center()
        self.show()
        
    def submit_register(self):
        self.submit = QPushButton("Login", self)
        self.submit.setToolTip("Press to enter selections!")
        self.submit.move(self.x+30,self.y+300)
        
        self.submit.clicked.connect(self.submit_clicked)

        self.register = QPushButton("Register", self)
        self.register.setToolTip("Press to register!")
        self.register.move(self.x+120,self.y+300)

        self.register.clicked.connect(self.register_clicked)
        
    def register_clicked(self):
        self.dialog = rp.registerUser()
        self.dialog.show()
        self.close()
    
    def submit_clicked(self):
        username = self.textbox1.text()
        password = self.textbox2.text()
        #print items above to see if working
        print(username)
        print(password) 
        db = sql3.connect('appDB.db')
        cr = db.cursor()
        try:
            assert cr.execute("SELECT * from users")
            #check if the table exists
        except sql3.OperationalError:
            print('No such database exists')
            #print above if it does not exist
            #you may want to print this in a message box in a GUI
            QMessageBox.warning(self,"ALERT","Database Table Does Not Exist")
        else:
            cr.execute("SELECT username, password FROM users")
            x=0
            for row in cr:
                #print('{},{},{},{},{}'.format(row[0], row[1], row[2],row[3],row[4]))
                if str(row[0]) == username and str(row[1]) == password:
                    x=1
                else:
                    continue           
            if x == 1:
                print("user exist!")
                self.textbox1.clear()
                self.textbox2.clear()
                self.dialog = ap.appMenu()
                self.dialog.show()
                self.close()
            else:
                QMessageBox.information(self,"ALERT","Invalid/unregistered username and/or password")
                print("user does not exist. You should register!")
        db.close()
        
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
'''
    code to create database from the start of loginpage.
    It is already expected that the database will exist
    so one will just need to connect to it
 
db = sql3.connect('appDB.db')
try:
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users"+
                "(userId INTEGER PRIMARY KEY AUTOINCREMENT,firstName TEXT,lastName TEXT,"+
                "age INTEGER, username TEXT, password TEXT, email TEXT, phone TEXT)")
    print("Table successfully created")
    
except:
     print("error in Table creation")
     db.rollback()
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = loginUser()
    sys.exit(app.exec_())
   
'''
    another way of checking if the user and the password entered
    by the user is in the database. The user will be a list 
    of tuples, wherein the tuples will have the elements of a row.
    Depending on which column is the usernam and the password,
    one can use a for loop to iterate each tuple and find the username
    and password and if any of them matches that of the login details
        
db = sql3.connect(addDB.db)
cr = db.cursor()
cr.execute("SELECT * from users")
user = cr.fetchall()
db.commit()
print(user)
for i in user:
    if i[1] == 'Linda' i[3] = 'JEB50239812':
        print("this is Linda")
        self.dialog = *name of module.name of class*
        self.dialog.show()
        self.close()
        
    else:
        print("This is not Linda")
        
db.close()
'''

'''
    another way to check if the table exists:

        
try:
    assert cr.execute("SELECT * from users")
    #check if the table exists
except sl3.OperationalError:
    print('No such database exists')
    #print above if it does not exist
    #you may want to print this too in a message box in a GUI
else:
    #if it exists
    #if it exists acess the database and manipulate it/reference it
    
'''
     