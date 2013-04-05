#!/usr/bin/env python
""":mod:`caesar_cipher.qt.main` -- Caesar cipher Qt main
"""

import sys

from PySide import QtGui

from caesar_cipher.utils import parse_arguments
from caesar_cipher.models import ApplicationModel
from caesar_cipher.qt.views import ApplicationView
from caesar_cipher.presenters import ApplicationPresenter


def main(argv):
    """Program entry point.

    :param argv: argument vector
    :type argv: :class:`list`
    :return: status code
    :rtype: :class:`int`
    """
    app = QtGui.QApplication(argv)
    parse_arguments(argv)

    model = ApplicationModel()
    view = ApplicationView()
    presenter = ApplicationPresenter(model, view)
    presenter.register_for_events()
    model.run()

    return app.exec_()

if __name__ == '__main__':
    raise SystemExit(sys.argv)
