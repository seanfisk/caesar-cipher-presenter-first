#!/usr/bin/env python
""":mod:`caesar_cipher.curses.main` -- Caesar cipher curses main
"""

import sys

from caesar_cipher.utils import parse_arguments
from caesar_cipher.models import ApplicationModel
from caesar_cipher.curses.views import ApplicationView
from caesar_cipher.presenters import ApplicationPresenter


def main(argv):
    """Program entry point.

    :param argv: argument vector
    :type argv: :class:`list`
    :return: status code
    :rtype: :class:`int`
    """
    parse_arguments(argv)
    model = ApplicationModel()
    view = ApplicationView()
    presenter = ApplicationPresenter(model, view)
    presenter.register_for_events()
    model.run()

if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
