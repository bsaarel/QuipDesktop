import sys
from PyQt5 import QtWidgets, QtCore

class Rings(QtWidgets.QWidget):
    
    def __init__(self):
        super(Rings, self).__init__()
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300,300,355,280)
        self.setWindowTitle('Rings')
        self.show()
        
    def paintEvent(self, e):
        
        painter = QtWidgets.QPainter()
        painter.begin(self)
        self.drawRings(painter)
        painter.end()
        
    def drawRings(self,painter):
        
        color = QtCore.Qt.black
        painter.setPen(color)
        "painter.setBrush(color)"
        painter.drawEllipse(QtCore.QPointF(100,100),50,50)
        
def main():
    
    app = QtWidgets.QApplication(sys.argv)
    ex = Rings()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()