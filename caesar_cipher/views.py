from PySide import QtCore, QtGui
import metadata


class ApplicationView(QtGui.QMainWindow):

    submitted = QtCore.Signal(str, str)
    text_changed = QtCore.Signal(str, str)
    auto_encrypt_toggled = QtCore.Signal(bool)

    def __init__(self, parent=None):
        super(ApplicationView, self).__init__(parent)

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
        self.text_input = QtGui.QPlainTextEdit(self.centralWidget())
        self.text_input.textChanged.connect(self.text_input_changed)
        self.layout.addRow('Text', self.text_input)
        self.key_input = QtGui.QLineEdit(self.centralWidget())
        self.layout.addRow('Key', self.key_input)
        self.auto_encrypt = QtGui.QCheckBox()
        self.auto_encrypt.stateChanged.connect(self.auto_encrypt_state_changed)
        self.layout.addRow('Auto-Encrypt', self.auto_encrypt)
        self.result_output = QtGui.QPlainTextEdit(self.centralWidget())
        self.result_output.setReadOnly(True)
        self.layout.addRow('Result', self.result_output)
        self.submit_button = QtGui.QPushButton('Encode', self.centralWidget())
        self.submit_button.clicked.connect(self.submit_clicked)
        self.layout.addRow(self.submit_button)

        # Show it!
        self.show()
        self.raise_()

    def about(self):
        """Create and show the about dialog."""
        AboutDialog(self).exec_()

    def get_text(self):
        return self.text_input.toPlainText()

    def get_key(self):
        return self.key_input.text()

    def set_result(self, result):
        self.result_output.setPlainText(result)

    def show_error(self, message):
        error_dialog = QtGui.QErrorMessage(self)
        error_dialog.showMessage(message)

    def submit_clicked(self):
        self.submitted.emit(self.get_text(), self.get_key())

    def auto_encrypt_state_changed(self, int):
        self.auto_encrypt_toggled.emit(self.auto_encrypt.isChecked())

    def text_input_changed(self):
        self.text_changed.emit(self.get_text(), self.get_key())


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
