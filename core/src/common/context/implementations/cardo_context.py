import uuid
from typing import Union

from pyspark.sql import SparkSession

from core.src.common.context.IContext import IContext
from core.src.common.helpers.logging.cardo_logger import cardo_logger
from core.src.common.helpers.mode import Mode
from core.src.common.helpers.singleton import Singleton


class CardoContext(IContext, metaclass=Singleton):
    def __init__(self, mode: Union[Mode, str] = Mode.POLARS):
        self.logger = cardo_logger.get_logger()
        self.run_id = str(uuid.uuid1()).lower()
        self.mode = mode
        if mode == Mode.SPARK:
            import libs.src.steps.spark as spark_steps
            self.steps = spark_steps
            self.spark = SparkSession.builder.master("local").getOrCreate()
        if mode == Mode.POLARS:
            import libs.src.steps.polars as polars_steps



    def get_context(self):
        self.logger.info(f"Starting cardo context in {self.mode} mode with run_id: {self.run_id}")
        return self
