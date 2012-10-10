#!/usr/bin/env python

# Test runner

import sys
import unittest

def main():
    """Runs unit test discovery. Equivalent to this on the
    command-line::

        python -m unittest discover tests

    No need to return anything since :func:`unittest.main()` directly
    calls :func:`sys.exit()`.

    """
    unittest.main(argv=['', 'discover', 'tests'])

if __name__ == '__main__':
    main()
