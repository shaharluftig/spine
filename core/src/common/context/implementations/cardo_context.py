import uuid

from pyspark.sql import SparkSession

from core.src.common.context.IContext import IContext
from core.src.common.helpers.logging.cardo_logger import CardoLogger
from core.src.common.helpers.singleton import Singleton


class CardoContext(IContext, metaclass=Singleton):
    def __init__(self, spark_session: SparkSession = None):
        self.logger = CardoLogger().get_logger()
        self.run_id = str(uuid.uuid1()).lower()
        if spark_session:
            self.spark_session = spark_session

    def get_context(self):
        self.logger.info("Starting cardo context")
        return self
