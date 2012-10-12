import unittest

from ludibrio import Mock

from caesar_cipher.presenters import init_presenters, ApplicationPresenter

class TestInitPresenters(unittest.TestCase):
    def test_init_presenters(self):
        with Mock() as caesar_cipher:
            from caesar_cipher.presenters import ApplicationPresenter
            ApplicationPresenter() >> None
        init_presenters()
        caesar_cipher.validate()

class TestApplicationPresenter(unittest.TestCase):
    def setUp(self):
        self.mock_model = Mock()
        self.mock_view = Mock()
        self.presenter = ApplicationPresenter(self.mock_model, self.mock_view)

    def test_register_for_events(self):
        with self.mock_view:
            self.mock_view.when_user_submits(
                self.presenter.user_submits) >> None
        with self.mock_model:
            pass
        self.presenter.register_for_events()

    def tearDown(self):
        self.mock_model.validate()
        self.mock_view.validate()
