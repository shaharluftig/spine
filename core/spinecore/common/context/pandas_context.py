from spinecore.common.context.base_context import BaseContext


class SpinePandasContext(BaseContext):
    def __init__(self, config: dict):
        super().__init__()
        self.__setup_config(config)

    @staticmethod
    def __setup_config(config: dict):
        """Sets pandas config from dict"""
        if config:
            import pandas as pd
            for key, value in config.items():
                pd.set_option(key, value)

    @staticmethod
    def get_context(config: dict = None):
        """Get or create SpinePandasContext"""
        ctx = SpinePandasContext(config)
        ctx.logger.info(f"Starting SpinePandasContext")
        return ctx

    @staticmethod
    def into_spark(spark_config: dict = {}, spark_session=None):
        """Converts SpinePandasContext to SpineSparkContext"""
        try:
            spark_config = {} if not spark_config else spark_config
            from spinecore.common.context.spark_context import SpineSparkContext
            return SpineSparkContext(spark_session, spark_config)
        except ImportError:
            raise ImportError("Pyspark must be installed in order to use SpineSparkContext")
