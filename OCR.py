# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QDialog()
   b1 = QPushButton(win)
   b1.setText("Brows")
   b1.move(50,10)
   b1.clicked.connect(b1_clicked)

#   b2 = QPushButton(win)
#   b2.setText("Convert to text")
#   b2.move(200,10)
#   QObject.connect(b2,SIGNAL("clicked()"),b2_clicked)
   
   #inserting picture pox 
   pic = QLabel(win)
   pic.setGeometry(70,5,700,500)
   pixmap = QPixmap(FILENAME)
   pixmap = pixmap.scaledToHeight(200)
   pic.setPixmap(pixmap)


   #win.setGeometry(0,0,1500,1500)
   win.setWindowTitle("PyQt")
   win.showMaximized()
   sys.exit(app.exec_())
o
def b1_clicked():
   print ("Button 1 clicked")

#def b2_clicked():
#   print ("Button 2 clicked")



FILENAME = 'ocr-a-font-sample.png'
#if __name__ == '__main__':
window()

