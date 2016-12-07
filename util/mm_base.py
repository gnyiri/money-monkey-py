from .mm_logger import MMLogger
from .mm_app import MMApp


class MMBase(object):
    """
    Base class for all PM classes
    """
    def __init__(self):
        self._logger = MMLogger.get_instance()
        self._app = MMApp.get_instance()

    @property
    def logger(self):
        return self._logger

    @property
    def app(self):
        return self._app
