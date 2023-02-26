import uuid
from typing import List

from core.src.common.context.IContext import IContext
from core.src.common.helpers.logging import Logger
from core.src.common.helpers.logging.implementations.cardo_logger import CardoLogger
from core.src.common.helpers.singleton import Singleton


class BaseContext(IContext, metaclass=Singleton):
    def __init__(self, logger: Logger = CardoLogger, log_handlers: List = []):
        self.run_id = str(uuid.uuid1()).lower()
        self.__cardo_logger = logger(self.run_id, log_handlers)
        self.logger = self.__cardo_logger.logger

    def get_cardo_logger(self) -> Logger:
        return self.__cardo_logger

    @staticmethod
    def get_context(log_handlers: List = []):
        ctx = BaseContext(log_handlers=log_handlers)
        return ctx
