#!/usr/bin/env python

# Test runner

import sys
import unittest

test_all = unittest.TestLoader().discover('tests')

def main():
    """Run all discovered unit tests."""
    result = unittest.TextTestRunner().run(test_all)
    sys.exit(not result.wasSuccessful())

if __name__ == '__main__':
    main()
