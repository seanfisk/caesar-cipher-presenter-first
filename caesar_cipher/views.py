from PySide import QtGui
import metadata


class ApplicationView(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(ApplicationView, self).__init__(parent)

        self.submit_callback = None
        self.setCentralWidget(QtGui.QWidget(self))

        # Menu
        self.menu_bar = QtGui.QMenuBar()
        self.file_menu = self.menu_bar.addMenu('&File')
        self.quit_action = self.file_menu.addAction('&Quit')
        self.quit_action.triggered.connect(self.close)
        self.help_menu = self.menu_bar.addMenu('&Help')
        self.about_action = self.help_menu.addAction('&About')
        self.about_action.triggered.connect(self.about)
        self.setMenuBar(self.menu_bar)

        # Layout
        self.layout = QtGui.QFormLayout(self.centralWidget())
        self.message_input = QtGui.QLineEdit(self.centralWidget())
        self.layout.addRow('Message', self.message_input)
        self.key_input = QtGui.QLineEdit(self.centralWidget())
        self.layout.addRow('Key', self.key_input)
        self.result = QtGui.QLabel(self.centralWidget())
        self.layout.addRow('Result', self.result)
        self.submit = QtGui.QPushButton('Encode', self.centralWidget())
        self.layout.addRow(self.submit)

        # Show it!
        self.show()
        self.raise_()

    def about(self):
        """Create and show the about dialog."""
        AboutDialog(self).exec_()

    def when_user_submits(self, callback):
        if self.submit_callback:
            self.submit.clicked.disconnect(self.submit_callback)
        self.submit_callback = callback
        self.submit.clicked.connect(self.submit_callback)

    def get_message(self):
        return self.message_input.text()

    def get_key(self):
        return self.key_input.text()

    def set_result(self, result):
        self.result.setText(result)


class AboutDialog(QtGui.QDialog):
    """Shows information about the program."""
    def __init__(self, parent=None):
        """Construct the dialog."""
        super(AboutDialog, self).__init__(parent)
        self.setWindowTitle('About ' + metadata.nice_title)
        self.layout = QtGui.QVBoxLayout(self)
        self.title_label = QtGui.QLabel(metadata.nice_title, self)
        self.layout.addWidget(self.title_label)
        self.version_label = QtGui.QLabel('Version ' + metadata.version, self)
        self.layout.addWidget(self.version_label)
        self.copyright_label = QtGui.QLabel('Copyright (C) ' +
                                            metadata.copyright, self)
        self.layout.addWidget(self.copyright_label)
        self.url_label = QtGui.QLabel(
            '<a href="{0}">{0}</a>'.format(metadata.url), self)
        self.url_label.setOpenExternalLinks(True)
        self.layout.addWidget(self.url_label)
