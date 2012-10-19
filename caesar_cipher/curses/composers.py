""":mod:`caesar_cipher.curses.composers` --- Create curses presenters
"""

from caesar_cipher.models import ApplicationModel
from caesar_cipher.curses.views import ApplicationView
from caesar_cipher.presenters import ApplicationPresenter


def create_application_presenter():
    """Create an MVP triad for a curses-based application presenter.

    :return: the created presenter
    :rtype: :class:`ApplicationPresenter`
    """
    model = ApplicationModel()
    view = ApplicationView()
    presenter = ApplicationPresenter(model, view)
    presenter.register_for_events()
    model.run()
    return presenter
