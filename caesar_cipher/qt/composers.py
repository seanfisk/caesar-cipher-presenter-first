""":mod:`caesar_cipher.composers` --- Functions to create Qt presenters
"""

from caesar_cipher.models import ApplicationModel
from caesar_cipher.qt.views import ApplicationView
from caesar_cipher.presenters import ApplicationPresenter


def create_application_presenter():
    """Create an MVP triad for a Qt-based application presenter.

    :return: the created presenter
    :rtype: :class:`ApplicationPresenter`
    """
    presenter = ApplicationPresenter(ApplicationModel(), ApplicationView())
    presenter.register_for_events()
    return presenter
