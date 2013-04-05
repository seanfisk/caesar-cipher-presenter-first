#!/usr/bin/env python
""":mod:`caesar_cipher.curses.main` -- Caesar cipher curses main
"""

import sys

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

    parse_arguments(argv)

    # To be safe, assign the presenter to a variable so it is not thrown away
    # by the Python garbage collector, which uses reference counting.
    presenter = create_application_presenter()  # NOQA

if __name__ == '__main__':
    sys.exit(main())
