import unittest

from mock import MagicMock, sentinel

from caesar_cipher.presenters import ApplicationPresenter


class TestApplicationPresenter(unittest.TestCase):
    def setUp(self):
        self.mock_model = MagicMock()
        self.mock_view = MagicMock()
        self.presenter = ApplicationPresenter(self.mock_model, self.mock_view)

    def test_register_for_events(self):
        self.presenter.register_for_events()

        self.mock_view.submitted.\
            connect.assert_called_once_with(self.presenter._user_submits)
        self.mock_view.auto_encrypt_toggled.\
            connect.assert_called_once_with(
                self.presenter._auto_encrypt_toggled)

    def test_auto_encrypt_on(self):
        self.presenter._auto_encrypt_toggled(True)
        self.mock_view.text_changed.connect.assert_called_once_with(
            self.presenter._user_submits)

    def test_auto_encrypt_off(self):
        self.presenter._auto_encrypt_toggled(False)
        self.mock_view.text_changed.disconnect.assert_called_once_with(
            self.presenter._user_submits)

    def test_user_submits_correct_format(self):
        self.mock_view.get_key.return_value = '1'
        self.mock_view.get_message.return_value = 'abcd'
        self.mock_model.caesar_encode.return_value = 'bcde'

        self.presenter._user_submits()

        self.mock_view.get_key.assert_called_once_with()
        self.mock_view.get_message.assert_called_once_with()
        self.mock_model.caesar_encode.assert_called_once_with('abcd', 1)
        self.mock_view.set_result.assert_called_once_with('bcde')

    def test_user_submits_empty_key(self):
        self.mock_view.get_key.return_value = ''

        self.presenter._user_submits()

        self.mock_view.get_key.assert_called_once_with()
        self.mock_view.show_error.assert_called_once_with(
            'Please enter a valid integer for the key.')

    def test_user_submits_alpha_key(self):
        self.mock_view.get_key.return_value = 'abcd'

        self.presenter._user_submits()

        self.mock_view.get_key.assert_called_once_with()
        self.mock_view.show_error.assert_called_once_with(
            'Please enter a valid integer for the key.')
