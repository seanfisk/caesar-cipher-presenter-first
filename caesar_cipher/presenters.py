class ApplicationPresenter(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def register_for_events(self):
        self.view.submitted.connect(self._user_submits)
        self.view.auto_encrypt_toggled.connect(self._auto_encrypt_toggled)

    def _auto_encrypt_toggled(self, switch_on):
        if switch_on:
            self.view.text_changed.connect(self._user_submits)
        else:
            self.view.text_changed.disconnect(self._user_submits)

    def _user_submits(self):
        try:
            key_int = int(self.view.get_key())
        except ValueError:
            self.view.show_error('Please enter a valid integer for the key.')
            return
        result = self.model.caesar_encode(self.view.get_message(), key_int)
        self.view.set_result(result)
