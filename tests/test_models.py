import unittest

import mock

from caesar_cipher.models import ApplicationModel
from caesar_cipher.utils import Event


class TestRun(unittest.TestCase):
    def setUp(self):
        self.model = ApplicationModel()

    def test_run(self):
        mock_on_started = mock.MagicMock(spec=Event, spec_set=True)
        self.model.started.append(mock_on_started)
        self.model.run()
        mock_on_started.assert_called_once_with()


class TestCaesarEncode(unittest.TestCase):
    def setUp(self):
        self.model = ApplicationModel()

    def test_nothing(self):
        result = self.model.caesar_encode('', 1)
        self.assertEqual(result, '')

    def test_bananas(self):
        result = self.model.caesar_encode('bananas', 1)
        self.assertEqual(result, 'cbobobt')

    def test_abcde(self):
        result = self.model.caesar_encode('abcde', 13)
        self.assertEqual(result, 'nopqr')

    def test_gwizdz(self):
        result = self.model.caesar_encode('gwizdz', 1)
        self.assertEqual(result, 'hxjaea')

    def test_uppercase(self):
        result = self.model.caesar_encode('ABCDE', -1)
        self.assertEqual(result, 'ZABCD')

    def test_upper_lower(self):
        result = self.model.caesar_encode('AbCdE', 1)
        self.assertEqual(result, 'BcDeF')

    def test_boundary(self):
        result = self.model.caesar_encode('AaZz', 2)
        self.assertEqual(result, 'CcBb')

    def test_odd_chars(self):
        result = self.model.caesar_encode('#ABCD!', 1)
        self.assertEqual(result, '#BCDE!')

    def test_sentence(self):
        result = self.model.caesar_encode('python testing is awesome', 13)
        self.assertEqual(result, 'clguba grfgvat vf njrfbzr')

    def test_phrase(self):
        result = self.model.caesar_encode(
            'I like my messages de-ciphered.', -10)
        self.assertEqual(result, 'Y byau co cuiiqwui tu-syfxuhut.')
