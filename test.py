#!/usr/bin/env python

# Test runner and style checker

from __future__ import print_function
import sys
import unittest
import argparse

import pep8

CODE_DIRECTORY = 'caesar_cipher'
TESTS_DIRECTORY = 'tests'
CHECK_FILES = [CODE_DIRECTORY,
               TESTS_DIRECTORY,
               'setup.py',
               'test.py']

test_all = unittest.TestLoader().discover(TESTS_DIRECTORY)


def run_tests():
    """Run all discovered unit tests."""
    result = unittest.TextTestRunner(stream=sys.stdout).run(test_all)
    return result.wasSuccessful()


def run_pep8():
    """Run PEP8 style guide checker on code and test files."""
    pep8_style = pep8.StyleGuide()
    report = pep8_style.check_files(CHECK_FILES)
    return report.total_errors == 0


def make_header(text):
    return text + '\n' + '=' * len(text) + '\n'


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) == 1:
        tests = True
        pep8 = True
    else:
        arg_parser = argparse.ArgumentParser(
            description='Test runner and style checker')
        arg_parser.add_argument('check', metavar='CHECK',
                                choices=['tests', 'pep8'],
                                help='What check to run (tests | pep8).')
        args = arg_parser.parse_args(args=argv[1:])
        tests = args.check == 'tests'
        pep8 = args.check == 'pep8'

    success = True
    if tests:
        print(make_header('Tests'))
        success &= run_tests()
        print()
    if pep8:
        print(make_header('Style Check'))
        pep8_success = run_pep8()
        if pep8_success:
            print('No style errors')
        success &= pep8_success

    return int(not success)

if __name__ == '__main__':
    sys.exit(main())
