#!/usr/bin/env python
""":mod:`caesar_cipher.curses.main` -- Caesar cipher curses main
"""

import sys

import urwid

from caesar_cipher.utils import parse_arguments
from caesar_cipher.curses.composers import create_application_presenter


def main(argv=None):
    """Program entry point.

    :param argv: argument vector
    :type argv: :class:`list`
    :return: status code
    :rtype: :class:`int`
    """
    if argv is None:
        argv = sys.argv

    args = parse_arguments(argv)

    presenter = create_application_presenter()

if __name__ == '__main__':
    sys.exit(main())
