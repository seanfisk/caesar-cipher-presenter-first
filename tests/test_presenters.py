import unittest
from mock import MagicMock, create_autospec

from caesar_cipher.presenters import ApplicationPresenter
from caesar_cipher.models import ApplicationModel


class TestApplicationPresenter(unittest.TestCase):
    def setUp(self):
        self.mock_model = create_autospec(ApplicationModel, spec_set=True)
        self.mock_view = MagicMock()
        self.presenter = ApplicationPresenter(self.mock_model, self.mock_view)

    def test_auto_encrypt_on(self):
        self.presenter._auto_encrypt_toggled(True)
        self.mock_view.text_changed.append.assert_called_once_with(
            self.presenter._user_submits)

    def test_auto_encrypt_off(self):
        self.presenter._auto_encrypt_toggled(False)
        self.mock_view.text_changed.remove.assert_called_once_with(
            self.presenter._user_submits)

    def test_user_submits_correct_format(self):
        self.mock_model.caesar_encode.return_value = 'bcde'

        self.presenter._user_submits('abcd', '1')

        self.mock_model.caesar_encode.assert_called_once_with('abcd', 1)
        self.mock_view.set_result.assert_called_once_with('bcde')

    def test_user_submits_empty_key(self):
        self.presenter._user_submits('fake message', '')

        self.mock_view.show_error.assert_called_once_with(
            'Please enter a valid integer for the key.')

    def test_user_submits_alpha_key(self):
        self.presenter._user_submits('fake message', 'alpha key')

        self.mock_view.show_error.assert_called_once_with(
            'Please enter a valid integer for the key.')
