import unittest

from mock import patch, sentinel, call, MagicMock


# We don't want to require PySide.QtGui for testing, since we are not
# testing our user interface. However, we may require PySide.QtCore
# since we are using Qt's signals and slots mechanism.
@patch('PySide.QtGui', MagicMock())
class TestCreateQtPresenter(unittest.TestCase):

    @patch('caesar_cipher.composers.ApplicationPresenter', autospec=True)
    @patch('caesar_cipher.composers.ApplicationView', autospec=True)
    @patch('caesar_cipher.composers.ApplicationModel', autospec=True)
    def test_create_qt_presenter(self, mock_model, mock_view, mock_presenter):
        mock_model.return_value = sentinel.model
        mock_view.return_value = sentinel.view
        presenter = mock_presenter.return_value

        from caesar_cipher.composers import create_qt_presenter
        retval = create_qt_presenter()
        self.assertEqual(retval, presenter)

        mock_model.assert_called_once_with()
        mock_view.assert_called_once_with()
        expected_presenter_calls = \
            call(sentinel.model, sentinel.view).\
            register_for_events().call_list()
        self.assertEqual(mock_presenter.mock_calls, expected_presenter_calls)
