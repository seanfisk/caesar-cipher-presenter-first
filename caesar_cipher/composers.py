""":mod:`caesar_cipher.composers` --- Functions to create presenters
"""

from caesar_cipher.models import ApplicationModel
from caesar_cipher.views import ApplicationView
from caesar_cipher.presenters import ApplicationPresenter


def create_qt_presenter():
    """Create an MVP triad for a Qt-based application presenter."""
    ApplicationPresenter(ApplicationModel(), ApplicationView())
