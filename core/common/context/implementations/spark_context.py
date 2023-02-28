from pyspark.sql import SparkSession

from core.common.context import BaseContext


class GarnetSparkContext(BaseContext):
    def __init__(self, spark_session: SparkSession):
        super().__init__()
        self.spark = self.setup_spark_session(spark_session)

    @staticmethod
    def setup_spark_session(spark_session: SparkSession):
        if spark_session:
            return spark_session
        return SparkSession.builder.master("local").getOrCreate()

    @staticmethod
    def get_context(spark_session: SparkSession = None):
        ctx = GarnetSparkContext(spark_session)
        ctx.logger.info("Starting GarnetSparkContext")
        return ctx

    @staticmethod
    def into_polars(lazy=True, config: dict = None):
        from core.common.context.implementations.polars_context import GarnetPolarsContext
        return GarnetPolarsContext(lazy, config)
