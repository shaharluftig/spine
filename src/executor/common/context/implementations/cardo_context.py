from src.executor.common.context.IContext import IContext
from src.executor.helpers.singleton import Singleton


class CardoContext(IContext, metaclass=Singleton):
    def get_context(self, *args, **kwargs):
        return self
