# Test runner and style checker

from __future__ import absolute_import
from __future__ import print_function
import abc
import sys
import unittest as unittest_module

from py.io import TerminalWriter
import pep8 as pep8module
from shovel import task

sys.path.append('.')

CODE_DIRECTORY = 'caesar_cipher'
TESTS_DIRECTORY = 'tests'
CHECK_FILES = [CODE_DIRECTORY,
               TESTS_DIRECTORY,
               'setup.py',
               'shovel.py']

test_all_loader = unittest_module.TestLoader().discover(TESTS_DIRECTORY)


class TestRunner(object):
    """Abstract test runner base class."""
    __metaclass__ = abc.ABCMeta

    def __init__(self, terminal_writer=TerminalWriter()):
        self.terminal_writer = terminal_writer

    @abc.abstractproperty
    def name(self):
        """Return the lowercase name of the test runner.

        :return: the name
        :rtype: :class:`str`
        """
        return ''

    @abc.abstractproperty
    def title(self):
        """Return the proper title of the test runner.

        :return: the title
        :type: :class:`str`
        """
        return ''

    @abc.abstractmethod
    def run(self):
        """Run the test runner.

        :return: number of errors, or exit code (0 is success, >1 is failure)
        :rtype: :class:`int`
        """
        self.terminal_writer.sep('=', self.title())


class UnitTestRunner(TestRunner):
    """Runner for unittest unit tests."""
    def name(self):
        return 'tests'

    def title(self):
        return 'unittest tests'

    def run(self):
        """Run all unit tests.

        :return: whether tests were successful
        :rtype: :class:`int`
        """
        super(UnitTestRunner, self).run()
        result = unittest_module.TextTestRunner(
            stream=sys.stdout).run(test_all_loader)
        return int(not result.wasSuccessful())


class StyleGuideRunner(TestRunner):
    def name(self):
        return 'pep8'

    def title(self):
        return 'PEP8 Style Guide'

    def run(self):
        """Run PEP8 style guide checker on code and test files.

        :return: the number of errors
        :rtype: :class:`int`
        """
        super(StyleGuideRunner, self).run()
        pep8_style = pep8module.StyleGuide()
        report = pep8_style.check_files(CHECK_FILES)
        if report.total_errors == 0:
            print('No style errors')
        return report.total_errors


@task
def pep8():
    """Perform a PEP8 style check on the code."""
    sys.exit(StyleGuideRunner().run())


@task
def unittest():
    """Run all unit tests."""
    sys.exit(UnitTestRunner().run())


@task
def test_all():
    """Perform a style check and run all unit tests."""
    success = True
    for runner in TestRunner.__subclasses__():
        success &= runner().run() == 0
    sys.exit(int(not success))
