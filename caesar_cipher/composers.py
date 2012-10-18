""":mod:`caesar_cipher.composers` --- Functions to create presenters
"""

from caesar_cipher.models import ApplicationModel
from caesar_cipher.views import qt
from caesar_cipher.presenters import ApplicationPresenter


def create_qt_presenter():
    """Create an MVP triad for a Qt-based application presenter.

    :return: the created presenter
    :rtype: :class:`ApplicationPresenter`
    """
    presenter = ApplicationPresenter(ApplicationModel(), qt.ApplicationView())
    presenter.register_for_events()
    return presenter
