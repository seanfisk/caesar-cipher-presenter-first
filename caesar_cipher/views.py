from PySide import QtGui

class ApplicationView(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(ApplicationView,self).__init__(parent)
        
        self.submit_callback = None
        self.layout = QtGui.QFormLayout(self)
        
        self.message_input = QtGui.QLineEdit(self)
        self.layout.addRow('Message',self.message_input)
        
        self.key_input = QtGui.QLineEdit(self)
        self.layout.addRow('Key',self.key_input)
        
        self.result = QtGui.QLabel(self)
        self.layout.addRow('Result',self.result)
        
        self.submit = QtGui.QPushButton('Encode',self)
        self.layout.addRow(self.submit)
        
        self.show()
        self.raise_()
    
    def when_user_submits(self,callback):
        if self.submit_callback:
            self.submit.clicked.disconnect(self.submit_callback)
        self.submit_callback = callback
        self.submit.clicked.connect(self.submit_callback)

    def get_message(self):
        return self.message_input.text()

    def get_key(self):
        return int(self.key_input.text())

    def set_result(self,result):
        self.result.setText(result)