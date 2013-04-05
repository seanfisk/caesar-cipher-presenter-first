# Test runner and style checker

from __future__ import absolute_import
from __future__ import print_function
import sys
import unittest
import subprocess

from shovel import task

# Add the current directory to the path so we can find the `better_banner'
# module.
sys.path.append('.')

CODE_DIRECTORY = 'caesar_cipher'
TESTS_DIRECTORY = 'tests'
LINT_FILES = [CODE_DIRECTORY,
              TESTS_DIRECTORY,
              'setup.py',
              'shovel.py']

test_all_loader = unittest.TestLoader().discover(TESTS_DIRECTORY)


def _test():
    """Run the unit test suite and return a status code.

    :return: status code
    :rtype: :class:`int`
    """
    print('unit test suite\n===============')
    result = unittest.TextTestRunner(
        stream=sys.stdout).run(test_all_loader)
    return int(not result.wasSuccessful())


def _lint():
    """Perform a lint check using flake8 and return a status code.

    :return: status code
    :rtype: :class:`int`
    """
    print('flake8 lint check\n=================')
    # Flake8 doesn't have an easy way to run checks using a Python
    # function, so just fork off another process to do it.
    status_code = subprocess.call(['flake8', '--max-complexity=10'] +
                                  LINT_FILES)
    if status_code == 0:
        print('All good')
    return status_code


@task
def test():
    """Run the unit test suite."""
    raise SystemExit(_test())


@task
def lint():
    """Perform a lint check using flake8."""
    raise SystemExit(_lint())


@task
def test_all():
    """Run the unit test suite and lint check using flake8."""
    status_code = _lint()
    print()
    status_code += _test()
    raise SystemExit(status_code)


@task
def curses():
    """Run the curses-based interface."""
    from caesar_cipher.curses.main import main
    main([])


@task
def qt():
    """Run the Qt-based interface."""
    from caesar_cipher.qt.main import main
    main([])
