import unittest

from mock import MagicMock, patch

@patch.dict('sys.modules', {'PySide': MagicMock()})
class TestCreateQtPresenter(unittest.TestCase):

    @patch('caesar_cipher.composers.ApplicationPresenter', autospec=True)
    @patch('caesar_cipher.composers.ApplicationView', autospec=True)
    @patch('caesar_cipher.composers.ApplicationModel', autospec=True)
    def test_create_qt_presenter(self, mock_model, mock_view, mock_presenter):
        mock_model.return_value = 'fake model'
        mock_view.return_value = 'fake view'
        mock_presenter.return_value = 'fake presenter'

        from caesar_cipher.composers import create_qt_presenter
        create_qt_presenter()

        mock_model.assert_called_once_with()
        mock_view.assert_called_once_with()
        mock_presenter.assert_called_once_with('fake model', 'fake view')
