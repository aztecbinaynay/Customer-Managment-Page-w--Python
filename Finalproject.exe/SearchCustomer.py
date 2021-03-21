import AppMenu as am
import ShowCustomer as showC
import sqlite3 as sql3
import sys
from PyQt5.QtWidgets import (QMessageBox, QPushButton, QApplication, QWidget, 
                             QLineEdit, QDesktopWidget, QLabel, QListWidget,
                             QVBoxLayout, QListWidgetItem)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class searchCustomer(QWidget): #QWidget is the base class for all GUI elements in the PyQt5.

    def __init__(self):      
        super().__init__() #initializes the main window
        self.title = "Delete Customer Menu"
        self.x = 60
        self.y = 100
        self.width = 400
        self.height = 400
        #self.l_c = QListWidget(self)
        #self.l_c.setGeometry(self.x, self.y-15, 265, 220) 
        self.mainTitle()
        self.buttons()
        self.list_customer()
        self.initUI()
    
    def mainTitle(self):
        self.MainTitle = QLabel("Delete Customers", self)
        self.MainTitle.move(self.x+30, self.y-65)
        self.MainTitle.setFont(QFont('Times', 20))
        
    def buttons(self):       
        self.back_ = QPushButton("back", self)
        self.back_.setToolTip("Press to enter App Menu!")
        self.back_.move(self.x+100,self.y+260)
        self.back_.clicked.connect(self.back_clicked)
        
        self.delete_u = QPushButton("delete", self)
        self.delete_u.setToolTip("Press to delete a customer!")
        self.delete_u.move(self.x+100,self.y+230)
        self.delete_u.setStyleSheet('color: red;')
        self.delete_u.clicked.connect(self.deleteClicked)
        
        self.profile_s = QPushButton("profile", self)
        self.profile_s.setToolTip("Press to see profile of customer!")
        self.profile_s.move(self.x+100,self.y+200)
        self.profile_s.setStyleSheet('color: blue;')
        self.profile_s.clicked.connect(self.profile)
        
    def profile(self):
        try:
            self.item1 = self.item.split(', ')
            
        except AttributeError:     
            QMessageBox.information(self,"ALERT!", "You didn't select a customer")
        else:
            ln = self.item1[0]
            fn = self.item1[1]
            print(fn)
            print(ln)
            cb = sql3.connect('customerDB.db')
            cur = cb.cursor()
            cur.execute(f"SELECT firstName, lastName, age, job, salary, email, phone, picture FROM customers  WHERE lastName = '{ln}' AND firstName = '{fn}'");
            user1 = cur.fetchone()
            cb.commit()
            cb.close()
            self.dialog = showC.showEmployee(user1)
            self.dialog.show()
            self.close()
        
    def push(self, item):       
        self.item = item.text()
        
    def back_clicked(self):
        self.dialog = am.appMenu()
        self.dialog.show()
        self.close()
    
    def list_customer(self):
        self.listC = QListWidget(self)
        self.listC.setGeometry(self.x, self.y-30, 265, 220) 
        cb = sql3.connect('customerDB.db')
        cur = cb.cursor()
        cur.execute("SELECT lastName, firstName FROM customers")
        cb.commit()
        for row in cur:
            self.s = '{}, {}'.format(row[0], row[1])
            self.listC.addItem(self.s)
        cb.close()
        self.listC.sortItems(Qt.AscendingOrder)
        self.listC.itemClicked.connect(self.push)
    
    def deleteClicked(self):  
        '''
            one can also delete by clearing the list using self.l_c.clear() after
            the item has been erased in the database. Then use self.list_customer()
            at the end of this function to go over the QListWidget creation again.
            Make sure to place the QListWidget object instansiation and setGeometry
            function under the def __init__ method after all other attributes
        '''
        try:
            self.item1 = self.item.split(', ')
            print(self.item1)
            try:
                cb = sql3.connect('customerDB.db')
                cur = cb.cursor()
                cur.execute(f"DELETE FROM customers WHERE lastName = '{self.item1[0]}' AND firstName = '{self.item1[1]}'");
                cb.commit()
                print("record deleted successfully")
                cb.close()
                self.listC.takeItem(self.listC.currentRow())
                #self.l_c.clear()
            except:
                print("error in operation")
                cb.rollback()
            print("this button works")
        
        except AttributeError:     
            QMessageBox.information(self,"ALERT!", "You didn't select a customer")
        #self.list_customer()
        
   

    
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
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = searchCustomer()
    sys.exit(app.exec_())

