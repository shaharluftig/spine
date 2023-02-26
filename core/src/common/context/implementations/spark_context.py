from pyspark.sql import SparkSession

from core import BaseContext
from core.src.common.context.implementations.polars_context import CardoPolarsContext


class CardoSparkContext(BaseContext):
    def __init__(self, spark_session: SparkSession):
        super().__init__()
        self.spark = spark_session

    @staticmethod
    def get_context(spark_session: SparkSession):
        ctx = CardoSparkContext(spark_session)
        ctx.logger.info("Starting Cardo-Spark context")
        return ctx

    @staticmethod
    def into_polars(lazy=True, config: dict = None) -> CardoPolarsContext:
        return CardoPolarsContext.get_context(lazy, config)
