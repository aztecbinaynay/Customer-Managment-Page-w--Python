import AppMenu as am
import sqlite3 as sql3
import sys
from PyQt5.QtWidgets import (QMessageBox, QPushButton, QApplication, QWidget, 
                             QLineEdit, QDesktopWidget, QLabel, QListWidget,
                             QVBoxLayout, QListWidgetItem)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class deleteUser(QWidget): #QWidget is the base class for all GUI elements in the PyQt5.

    def __init__(self):      
        super().__init__() #initializes the main window
        self.title = "Delete Admins Menu"
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
        self.MainTitle = QLabel("Delete Admins/Users", self)
        self.MainTitle.move(self.x+10, self.y-50)
        self.MainTitle.setFont(QFont('Times', 20))
        
    def buttons(self):       
        self.back_ = QPushButton("back", self)
        self.back_.setToolTip("Press to enter App Menu!")
        self.back_.move(self.x+100,self.y+260)
        self.back_.clicked.connect(self.back_clicked)
        
        self.delete_u = QPushButton("delete", self)
        self.delete_u.setToolTip("Press to delete an admin!")
        self.delete_u.move(self.x+100,self.y+230)
        self.delete_u.setStyleSheet('color: red;')
        self.delete_u.clicked.connect(self.deleteClicked)
        
    def push(self, item):       
        self.item = item.text()
        
    def back_clicked(self):
        self.dialog = am.appMenu()
        self.dialog.show()
        self.close()
    
    def list_customer(self):
        self.l_c = QListWidget(self)
        self.l_c.setGeometry(self.x, self.y-15, 265, 220) 
        db = sql3.connect('appDB.db')
        cr = db.cursor()
        cr.execute("SELECT lastName, firstName FROM users")
        db.commit()
        for row in cr:
            self.s = '{}, {}'.format(row[0], row[1])
            self.l_c.addItem(self.s)
        db.close()
        self.l_c.sortItems(Qt.AscendingOrder)
        self.l_c.itemClicked.connect(self.push)
    
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
                db = sql3.connect('appDB.db')
                cr=db.cursor()
                cr.execute(f"DELETE FROM users WHERE lastName = '{self.item1[0]}' AND firstName = '{self.item1[1]}'");
                db.commit()
                print("record deleted successfully")
                db.close()
                self.l_c.takeItem(self.l_c.currentRow())
                #self.l_c.clear()
            except:
                print("error in operation")
                db.rollback()
            print("this button works")
        
        except AttributeError:     
            QMessageBox.information(self,"ALERT!", "You didn't select a user")
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = deleteUser()
    sys.exit(app.exec_())
'''