""":mod:`caesar_cipher.views` --- Application user interface
"""

from PySide import QtCore, QtGui
from caesar_cipher import metadata


class ApplicationView(QtGui.QMainWindow):
    """Primary application view."""
    submitted = QtCore.Signal(str, str)
    text_changed = QtCore.Signal(str, str)
    auto_encrypt_toggled = QtCore.Signal(bool)

    def __init__(self, parent=None):
        """Construct a main view.

        :param parent: widget parent
        :type parent: :class:`QtGui.QWidget`
        """
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
        self.text_input.textChanged.connect(self._text_input_changed)
        self.layout.addRow('Text', self.text_input)
        self.key_input = QtGui.QLineEdit(self.centralWidget())
        self.layout.addRow('Key', self.key_input)
        self.auto_encrypt = QtGui.QCheckBox()
        self.auto_encrypt.stateChanged.connect(
            self._auto_encrypt_state_changed)
        self.layout.addRow('Auto-Encrypt', self.auto_encrypt)
        self.result_output = QtGui.QPlainTextEdit(self.centralWidget())
        self.result_output.setReadOnly(True)
        self.layout.addRow('Result', self.result_output)
        self.submit_button = QtGui.QPushButton('Encode', self.centralWidget())
        self.submit_button.clicked.connect(self._submit_clicked)
        self.layout.addRow(self.submit_button)

        # Show it!
        self.show()
        self.raise_()

    def about(self):
        """Create and show the about dialog."""
        AboutDialog(self).exec_()

    def get_text(self):
        """Return the widget's entered text.

        :return: the text
        :rtype: :class:`str`
        """
        return self.text_input.toPlainText()

    def get_key(self):
        """Return the widget's entered key.

        :return: the key
        :rtype: :class:`str`
        """
        return self.key_input.text()

    def set_result(self, result):
        """Set encoded text result.

        :param result: the encoded text
        :type result: :class:`str`
        """
        self.result_output.setPlainText(result)

    def show_error(self, message):
        """Show the user an error dialog.

        :param message: error message
        :type message: :class:`str`
        """
        error_dialog = QtGui.QErrorMessage(self)
        error_dialog.showMessage(message)

    def _submit_clicked(self):
        self.submitted.emit(self.get_text(), self.get_key())

    def _auto_encrypt_state_changed(self, int):
        self.auto_encrypt_toggled.emit(self.auto_encrypt.isChecked())

    def _text_input_changed(self):
        self.text_changed.emit(self.get_text(), self.get_key())


class AboutDialog(QtGui.QDialog):
    """Shows information about the program."""
    def __init__(self, parent=None):
        """Construct the dialog.

        :param parent: the widget's parent
        :type parent: :class:`QtGui.QWidget`
        """
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