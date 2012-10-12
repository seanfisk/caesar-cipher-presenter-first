import unittest

from ludibrio import Mock

from caesar_cipher.presenters import init_presenters

class TestInitPresenters(unittest.TestCase):
    def test_init_presenters(self):
        with Mock() as caesar_cipher:
            from caesar_cipher.presenters import ApplicationPresenter
            ApplicationPresenter() >> None
        init_presenters()
        caesar_cipher.validate()
