import pyspark
from pyspark.sql import SparkSession

from core.common.context.base_context import BaseContext


class GarnetSparkContext(BaseContext):
    def __init__(self, spark_session: SparkSession, spark_config: dict):
        super().__init__()
        self.spark = self.__setup_spark_session(spark_session, spark_config)

    @staticmethod
    def __setup_spark_session(spark_session: SparkSession, spark_config: dict):
        if spark_session:
            return spark_session
        return SparkSession.builder.config(conf=pyspark.SparkConf().setAll(spark_config.items())) \
            .enableHiveSupport().getOrCreate()

    @staticmethod
    def get_context(spark_config=None, spark_session: SparkSession = None):
        spark_config = {} if not spark_config else spark_config
        ctx = GarnetSparkContext(spark_session, spark_config)
        ctx.logger.info("Starting GarnetSparkContext")
        return ctx

    @staticmethod
    def into_polars(lazy=True, config: dict = None):
        try:
            from core.common.context.polars_context import GarnetPolarsContext
            return GarnetPolarsContext(lazy, config)
        except ImportError:
            raise ImportError("Polars must be installed in order to use PolarsSparkContext")
