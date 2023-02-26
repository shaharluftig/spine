from pyspark.sql import SparkSession

from core import BaseContext


class CardoPolarsContext(BaseContext):
    def __init__(self, lazy: bool, config: dict):
        super().__init__()
        self.lazy = lazy
        self.__setup_config(config)

    @staticmethod
    def __setup_config(config: dict):
        """Sets polars config from dict"""
        # TODO: Make this less ugly
        if config:
            exec("import polars as pl")
            for key, value in config.items():
                exec(f"pl.Config.{key}({value})")

    @staticmethod
    def get_context(lazy: bool = True, config: dict = None):
        ctx = CardoPolarsContext(lazy, config)
        ctx.logger.info("Starting Cardo-Polars context")
        return ctx

    @staticmethod
    def into_spark(spark_session: SparkSession = None):
        """Converts CardoPolarsContext to CardoSparkContext"""
        from core.src.common.context.implementations.spark_context import CardoSparkContext
        return CardoSparkContext(spark_session)
