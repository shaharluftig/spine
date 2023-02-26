from pyspark.sql import SparkSession

from core import BaseContext
from core.src.common.context.implementations.spark_context import CardoSparkContext


class CardoPolarsContext(BaseContext):
    def __init__(self, lazy: bool):
        super().__init__()
        self.lazy = lazy

    @staticmethod
    def __setup_config(config: dict):
        if config:
            for key, value in config:
                exec(f"pl.Config.{key}({value})")

    @staticmethod
    def get_context(lazy: bool = True, polars_config: dict = None):
        ctx = CardoPolarsContext(lazy)
        ctx.__setup_config(polars_config)
        ctx.logger.info("Starting Cardo-Polars context")
        return ctx

    @staticmethod
    def into_spark(spark_session: SparkSession):
        return CardoSparkContext.get_context(spark_session)
