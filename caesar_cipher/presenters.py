""":mod:caesar_cipher.presenters --- Application presenters
"""


class ApplicationPresenter(object):
    """Primary application presenter."""
    def __init__(self, model, view):
        """Constructor.

        :param model: application model
        :type model: :class:`caesar_cipher.models.ApplicationModel`
        :param view: application view
        :type view: :class:`caesar_cipher.views.ApplicationView`
        """
        self.model = model
        self.view = view

    def register_for_events(self):
        """Connect view methods to presenter methods."""
        self.model.started.append(self.view.start)
        self.view.submitted.connect(self._user_submits)
        self.view.auto_encrypt_toggled.connect(self._auto_encrypt_toggled)

    def _auto_encrypt_toggled(self, switch_on):
        """Toggle auto-encrypt on or off.

        :param switch_on: boolean to indicate whether it is on
        :type switch_on: :class:`bool`
        """
        if switch_on:
            self.view.text_changed.connect(self._user_submits)
        else:
            self.view.text_changed.disconnect(self._user_submits)

    def _user_submits(self, text, key):
        """Handle user submission.

        :param text: text to encode
        :type text: :class:`str`
        :param key: key by which to encode
        :type key: :class:`str`
        """
        try:
            key_int = int(key)
        except ValueError:
            self.view.show_error('Please enter a valid integer for the key.')
            return
        result = self.model.caesar_encode(text, key_int)
        self.view.set_result(result)
