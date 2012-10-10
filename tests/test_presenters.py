import unittest

from ludibrio import Mock

from caesar_cipher.presenters import register_for_events

class TestPresenters(unittest.TestCase):
    def test_register_for_events(self):
        with Mock() as caesar_cipher:
            from caesar_cipher.application_presenter import register_events
            register_events() >> None
        register_for_events()
        caesar_cipher.validate()
