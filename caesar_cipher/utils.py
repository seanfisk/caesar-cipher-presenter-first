""":mod:`caesar_cipher.utils` --- Miscellaneous utilities
"""

import sys
import argparse

from caesar_cipher import metadata


def parse_arguments(argv):
    """Parse command-line arguments.

    :param argv: argument vector
    :type argv: :class:`list`
    :return: argument namespace
    :rtype: :class:`argparse.Namespace`
    """
    author_strings = []
    for name, email in zip(metadata.authors, metadata.emails):
        author_strings.append('Author: {0} <{1}>'.format(name, email))

    version = '{0} {1}'.format(metadata.nice_title, metadata.version)
    epilog = '''
{version}

{authors}
URL: <{url}>
'''.format(
        version=version,
        authors='\n'.join(author_strings),
        url=metadata.url)

    arg_parser = argparse.ArgumentParser(
        prog=metadata.title,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=metadata.description,
        epilog=epilog)
    arg_parser.add_argument('-V', '--version', action='version',
                            version=version)

    return arg_parser.parse_args(args=argv[1:])
