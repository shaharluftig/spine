from pyspark.sql import SparkSession

from core import BaseContext
from core.src.common.helpers.dataframe import SparkDataFrame


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
    def into_pandas(df: SparkDataFrame):
        return df.toPandas()

    def into_polars(self):
        pass
