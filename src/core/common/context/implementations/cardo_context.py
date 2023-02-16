from src.core.common.context.IContext import IContext
from src.core.helpers.singleton import Singleton


class CardoContext(IContext, metaclass=Singleton):
    def get_context(self, *args, **kwargs):
        return self
