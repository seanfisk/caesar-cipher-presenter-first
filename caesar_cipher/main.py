#!/usr/bin/env python
""":mod:`caesar_cipher.main` -- Caesar cipher main
"""

from __future__ import print_function
import sys
import argparse

from PySide import QtGui

from caesar_cipher import metadata
from caesar_cipher.composers import create_qt_presenter


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

    author_strings = []
    for name, email in zip(metadata.authors, metadata.emails):
        author_strings.append('Author: {0} <{1}>'.format(name, email))

    epilog = '''
{title} {version}

{authors}
URL: <{url}>
'''.format(
        title=metadata.nice_title,
        version=metadata.version,
        authors='\n'.join(author_strings),
        url=metadata.url)

    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=metadata.description,
        epilog=epilog)

    args = arg_parser.parse_args(args=argv[1:])

    presenter = create_qt_presenter()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
