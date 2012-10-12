def init_presenters():
    """Create all presenters."""
    ApplicationPresenter()

class ApplicationPresenter(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.register_for_events()

    def user_submits(self):
        pass

    def register_for_events(self):
        self.view.when_user_submits(self.user_submits)
