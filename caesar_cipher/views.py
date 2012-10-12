from PySide import QtGui

class ApplicationView(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(ApplicationView,self).__init__(parent)
        self.show()
        self.raise_()
    def when_user_submits(self,callback):
        pass