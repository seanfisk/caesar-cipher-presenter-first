import unittest

from mock import patch, sentinel, call, MagicMock

from caesar_cipher.curses.composers import create_application_presenter


class TestCreateApplicationPresenter(unittest.TestCase):
    @patch('caesar_cipher.curses.composers.ApplicationPresenter',
           autospec=True, spec_set=True)
    @patch('caesar_cipher.curses.composers.ApplicationView',
           autospec=True, spec_set=True)
    @patch('caesar_cipher.curses.composers.ApplicationModel',
           autospec=True, spec_set=True)
    def test_create_qt_presenter(self, mock_model, mock_view, mock_presenter):
        model = mock_model.return_value
        mock_view.return_value = sentinel.view
        presenter = mock_presenter.return_value

        retval = create_application_presenter()
        self.assertEqual(retval, presenter)

        expected_model_calls = call().run().call_list()
        self.assertEqual(mock_model.mock_calls, expected_model_calls)
        mock_view.assert_called_once_with()
        expected_presenter_calls = \
            call(model, sentinel.view).register_for_events().call_list()
        self.assertEqual(mock_presenter.mock_calls, expected_presenter_calls)
