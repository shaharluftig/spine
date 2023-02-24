import uuid

from pyspark.sql import SparkSession

from core.src.common.context.IContext import IContext
from core.src.common.helpers.logging import Logger
from core.src.common.helpers.logging.implementations.cardo_logger import CardoLogger
from core.src.common.helpers.singleton import Singleton


class CardoContext(IContext, metaclass=Singleton):
    def __init__(self, spark_session: SparkSession = None, logger: Logger = CardoLogger):
        self.run_id = str(uuid.uuid1()).lower()
        self.__cardo_logger = logger(self.run_id)
        self.logger = self.__cardo_logger.logger
        if spark_session:
            self.spark = spark_session

    def get_cardo_logger(self):
        return self.__cardo_logger

    @staticmethod
    def get_context(spark: SparkSession = None):
        ctx = CardoContext(spark)
        ctx.logger.info("Starting Cardo context")
        return ctx
