#!/usr/bin/env python
""":mod:`caesar_cipher.qt.main` -- Caesar cipher Qt main
"""

import sys

from PySide import QtGui

from caesar_cipher.utils import parse_arguments
from caesar_cipher.qt.composers import create_application_presenter


def main(argv=None):
    """Program entry point.

    :param argv: argument vector
    :type argv: :class:`list`
    :return: status code
    :rtype: :class:`int`
    """
    if argv is None:
        argv = sys.argv

    app = QtGui.QApplication(argv)

    args = parse_arguments(argv)

    presenter = create_application_presenter()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
