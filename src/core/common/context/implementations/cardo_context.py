import uuid

from src.core.common.context.IContext import IContext
from src.core.helpers.logging.cardo_logger import CardoLogger
from src.core.helpers.singleton import Singleton


class CardoContext(IContext, metaclass=Singleton):
    def __init__(self):
        self.logger = CardoLogger().get_logger()
        self.run_id = str(uuid.uuid1()).lower()


    def get_context(self, *args, **kwargs):
        self.logger.info("Starting cardo context")
        return self
