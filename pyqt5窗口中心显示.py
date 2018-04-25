#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
pyqt5 from the oho
"""
 
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        #这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))
        
        #创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('端口扫描')
        
        #创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('端口扫描', self)
        btn.setToolTip('全扫描模式')
        
        #btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())
        
        #移动窗口的位置
        btn.move(20, 20)       

        qbtn = QPushButton('退出', self)
        qbtn.setToolTip('退出')
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(20, 40)                         
        
        self.setGeometry(550, 550, 550, 550)
        self.setWindowTitle('端口扫描器 from one_have_one')    
        

       
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
