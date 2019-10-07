class BaseBlock:
    def __init__(self, app=None):
        self.app = app

        if self.app is not None and hasattr(self, "callbacks"):
            self.callbacks(self.app)
