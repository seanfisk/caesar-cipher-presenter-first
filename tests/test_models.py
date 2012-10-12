import unittest

from ludibrio import Mock

from caesar_cipher.models import ApplicationModel

class TestCaesarEncode(unittest.TestCase):
    def setUp(self):
        self.model = ApplicationModel()
    def test_nothing(self):
        result = self.model.caesar_encode('',1)
        self.assertEqual(result,'')
    def test_bananas(self):
        result = self.model.caesar_encode('bananas',1)
        self.assertEqual(result,'cbobobt')
    def test_abcde(self):
        result = self.model.caesar_encode('abcde',1)
        self.assertEqual(result,'bcdef')
    def test_gwizdz(self):
        result = self.model.caesar_encode('gwizdz',1)
        self.assertEqual(result,'hxjaea')
    def test_uppercase(self):
        result = self.model.caesar_encode('ABCDE',1)
        self.assertEqual(result,'BCDEF')
    def test_upper_lower(self):
        result = self.model.caesar_encode('AbCdE',1)
        self.assertEqual(result,'BcDeF')
    def test_boundary(self):
        result = self.model.caesar_encode('AaZz',2)
        self.assertEqual(result,'CcBb')