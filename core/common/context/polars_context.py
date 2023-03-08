from core.common.context.base_context import BaseContext


class SpinePolarsContext(BaseContext):
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
        """Get or create SpinePolars context"""
        ctx = SpinePolarsContext(lazy, config)
        ctx.logger.info(f"Starting SpinePolarsContext with lazy_mode={lazy}")
        return ctx

    @staticmethod
    def into_spark(spark_config: dict = {}, spark_session=None):
        """Converts SpinePolarsContext to SpineSparkContext"""
        try:
            spark_config = {} if not spark_config else spark_config
            from core.common.context.spark_context import SpineSparkContext
            return SpineSparkContext(spark_session, spark_config)
        except ImportError:
            raise ImportError("Pyspark must be installed in order to use SpineSparkContext")
