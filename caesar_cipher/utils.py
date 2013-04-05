""":mod:`caesar_cipher.utils` --- Miscellaneous utilities
"""

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


# credit: <http://stackoverflow.com/a/2022629>
class Event(list):
    """Event subscription.

    A list of callable objects. Calling an instance of this will cause a
    call to each item in the list in ascending order by index.

    Example usage::

        >>> def f(x):
        ...     print 'f({0})'.format(x)
        >>> def g(x):
        ...     print 'g({0})'.format(x)
        >>> e = Event()
        >>> e()
        >>> e.append(f)
        >>> e(123)
        f(123)
        >>> e.remove(f)
        >>> e()
        >>> e += (f, g)
        >>> e(10)
        f(10)
        g(10)
        >>> del e[0]
        >>> e(2)
        g(2)
    """
    def __call__(self, *args, **kwargs):
        for f in self:
            f(*args, **kwargs)

    def __repr__(self):
        return 'Event({0})'.format(list.__repr__(self))
