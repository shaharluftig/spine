
from core.common.context.base_context import BaseContext


class GarnetPolarsContext(BaseContext):
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
        """Get or create GarnetPolars context"""
        ctx = GarnetPolarsContext(lazy, config)
        ctx.logger.info("Starting GarnetPolarsContext")
        return ctx

    @staticmethod
    def into_spark(spark_config: dict = {}, spark_session=None):
        """Converts GarnetPolarsContext to GarnetSparkContext"""
        try:
            spark_config = {} if not spark_config else spark_config
            from core.common.context.spark_context import GarnetSparkContext
            return GarnetSparkContext(spark_session, spark_config)
        except ImportError:
            raise ImportError("Pyspark must be installed in order to use GarnetSparkContext")