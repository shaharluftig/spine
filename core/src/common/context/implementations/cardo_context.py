import uuid

from pyspark.sql import SparkSession

from core.src.common.context.IContext import IContext
from core.src.common.helpers.logging.cardo_logger import cardo_logger
from core.src.common.helpers.singleton import Singleton


class CardoContext(IContext, metaclass=Singleton):
    def __init__(self, spark_session: SparkSession = None):
        self.logger = cardo_logger.get_logger()
        self.run_id = str(uuid.uuid1()).lower()
        if spark_session:
            self.spark = spark_session

    def get_context(self):
        self.logger.info(f"Starting cardo context with run_id: {self.run_id}")
        return self
