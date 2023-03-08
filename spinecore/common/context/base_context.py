import uuid
from typing import List

from spinecore.common.helpers.contract.IContext import IContext
from spinecore.common.helpers.logging import SpineLogger
from spinecore.common.helpers.contract import Logger
from spinecore.common.helpers.contract.metaclasses.singleton import Singleton


class BaseContext(IContext, metaclass=Singleton):
    def __init__(self, logger: Logger = SpineLogger, log_handlers: List = []):
        self.run_id = str(uuid.uuid1()).lower()
        self.__spine_logger = logger(self.run_id, log_handlers)
        self.logger = self.__spine_logger.logger

    def get_spine_logger(self) -> SpineLogger:
        return self.__spine_logger

    @staticmethod
    def get_context(log_handlers: List = []):
        ctx = BaseContext(log_handlers=log_handlers)
        return ctx
