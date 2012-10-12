import unittest

from ludibrio import Mock

from caesar_cipher.presenters import ApplicationPresenter

class TestApplicationPresenter(unittest.TestCase):
    def setUp(self):
        self.mock_model = Mock()
        self.mock_view = Mock()
        self.presenter = ApplicationPresenter(self.mock_model, self.mock_view)

    def test_register_for_events(self):
        with self.mock_model:
            pass
        with self.mock_view:
            self.mock_view.when_user_submits(
                self.presenter.user_submits) >> None
        self.presenter.register_for_events()

    def test_user_submits(self):
        with self.mock_view:
            self.mock_view.get_message() >> 'abcd'
            self.mock_view.get_key() >> 1
            self.mock_view.set_result('bcde') >> None
        with self.mock_model:
            self.mock_model.caesar_encode('abcd', 1) >> 'bcde'
        self.presenter.user_submits()

    def tearDown(self):
        self.mock_model.validate()
        self.mock_view.validate()
