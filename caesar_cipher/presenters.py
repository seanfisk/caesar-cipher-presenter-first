class ApplicationPresenter(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.when_user_submits(self._user_submits)

    def _user_submits(self):
        result = self.model.caesar_encode(self.view.get_message(),
                                          int(self.view.get_key()))
        self.view.set_result(result)
