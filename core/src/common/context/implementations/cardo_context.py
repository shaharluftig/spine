import uuid
from typing import List

from pyspark.sql import SparkSession

from core.src.common.context.IContext import IContext
from core.src.common.helpers.logging import Logger
from core.src.common.helpers.logging.implementations.cardo_logger import CardoLogger
from core.src.common.helpers.singleton import Singleton


class CardoContext(IContext, metaclass=Singleton):
    def __init__(self, spark_session: SparkSession = None, lazy_polars: bool = True, logger: Logger = CardoLogger,
                 log_handlers: List = []):
        self.run_id = str(uuid.uuid1()).lower()
        self.__cardo_logger = logger(self.run_id, log_handlers)
        self.logger = self.__cardo_logger.logger
        self.lazy_polars = lazy_polars
        if spark_session:
            self.spark = spark_session

    def get_cardo_logger(self):
        return self.__cardo_logger

    @staticmethod
    def get_context(spark: SparkSession = None, lazy_polars: bool = True, log_handlers: List = []):
        ctx = CardoContext(spark, lazy_polars, log_handlers=log_handlers)
        ctx.logger.info("Starting Cardo context")
        return ctx
